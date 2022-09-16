# backend/inference.py

import config
from YOLOv7 import YOLOv7


def inference(model, image):
    model_name = f"{config.MODEL_PATH}{model}.onnx"

    # Initialize YOLOv7 object detector
    yolov7_detector = YOLOv7(model_name, conf_thres=0.3, iou_thres=0.5)

    boxes, scores, class_ids = yolov7_detector(image)

   # Draw detections
    output = yolov7_detector.draw_detections(image)

    return output