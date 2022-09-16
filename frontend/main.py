# frontend/main.py

import requests
import streamlit as st
from PIL import Image


STYLES = {
    "yolov7_256x320": "yolov7_256x320",
    "yolov7_256x480": "yolov7_256x480",
    "yolov7_256x640": "yolov7_256x640",
    "yolov7_384x640": "yolov7_384x640",
    "yolov7_480x640": "yolov7_480x640",
    "yolov7_640x640": "yolov7_640x640",
    "yolov7_736x1280": "yolov7_736x1280",
    "yolov7-tiny_256x320": "yolov7-tiny_256x320",
    "yolov7-tiny_256x480": "yolov7-tiny_256x480",
    "yolov7-tiny_256x640": "yolov7-tiny_256x640",
    "yolov7-tiny_384x640": "yolov7-tiny_384x640",
    "yolov7-tiny_480x640": "yolov7-tiny_480x640",
    "yolov7-tiny_640x640": "yolov7-tiny_640x640",
    "yolov7-tiny_736x1280": "yolov7-tiny_736x1280",
}

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Object Detection Web APP')

image = st.file_uploader('Choose an image')

style = st.selectbox('Choose the model', [i for i in STYLES.keys()])

if st.button('Detect'):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://backend:8080/{style}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get('name'))
        st.image(image)