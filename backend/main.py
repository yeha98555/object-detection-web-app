# backend/main.py

import uuid

import numpy as np
from PIL import Image
import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

import config
import inference


app = FastAPI()


@app.get('/')
def read_root():
    return {'message:': 'Welcome from the API'}

@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    model = config.STYLES[style]
    output = inference.inference(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    return {"name": name, "size": "{0} x {1}".format(*image.shape[:2])}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)