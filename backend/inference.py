# backend/inference.py

import uuid

import os
import config
import cv2
from YOLOv7 import YOLOv7


def init(model):
    model_name = f"{config.MODEL_PATH}{model}.onnx"

    # Initialize YOLOv7 object detector
    yolov7_detector = YOLOv7(model_name, conf_thres=0.3, iou_thres=0.5)

    return yolov7_detector

def inference_image(detector, image):
    boxes, scores, class_ids = detector(image)
    output = detector.draw_detections(image)

    return output

def inference_video(detector, image):
    cap = cv2.VideoCapture(image)
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = f"/storage/{str(uuid.uuid4())}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if not ret:
                break
        except Exception as e:
            print(e)
            continue

        # Update object localizer
        combined_img = inference_image(detector, frame)

        # cv2.imshow("Detected Objects", combined_img)
        out.write(combined_img)

    cap.release()
    out.release()

    output_path_h264 = output_path.replace('.mp4', '_h264.mp4')

    # Encode video streams into the H.264
    os.system('ffmpeg -i {} -vcodec libx264 {}'.format(output_path, output_path_h264))
    os.remove(output_path)

    return output_path_h264, width, height