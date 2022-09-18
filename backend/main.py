# backend/main.py

import uuid

import os
import numpy as np
from PIL import Image
import cv2
import uvicorn
from fastapi import File, FastAPI, UploadFile
from fastapi.concurrency import run_in_threadpool
import aiofiles

import config
import inference


app = FastAPI()


@app.get('/')
def read_root():
    return {'message:': 'Welcome from the API'}

@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    model = config.STYLES[style]
    detector = inference.init(model)

    image = np.array(Image.open(file.file))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    output = inference.inference_image(detector, image)
    image_path = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(image_path, output)

    return {"name": image_path, "size": "{0} x {1}".format(*image.shape[:2])}

@app.post("/video/{style}")
async def get_video(style: str, file: UploadFile = File(...)):
    model = config.STYLES[style]
    detector = inference.init(model)

    try:
        async with aiofiles.tempfile.NamedTemporaryFile(mode="wb", delete=False) as temp:
            try:
                contents = await file.read()
                await temp.write(contents)
            except Exception:
                return {"message": "There was an error uploading the file"}
            finally:
                await file.close()

        video_path, width, height = await run_in_threadpool(inference.inference_video, detector, temp.name)  # Pass temp.name to VideoCapture()
    except Exception:
        return {"message": "There was an error processing the file"}
    finally:
        os.remove(temp.name)
    
    return {"name": video_path, "size": "{0} x {1}".format(width, height)}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)