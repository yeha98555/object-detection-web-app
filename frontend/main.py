# frontend/main.py

import requests
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
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

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Object Detection Web APP')

filetype = st.radio('Choose the file type', ('Image', 'Video', 'Camera'))

if filetype == 'Image':
    image = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])
elif filetype == 'Video':
    image = st.file_uploader('Choose a video', type=['avi', 'mp4', 'mov'])
else:
    image = None
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

style = st.selectbox('Choose the model', [i for i in STYLES.keys()])

if st.button('Detect'):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        if (filetype == 'Image'):
            res = requests.post(f"http://backend:8080/{style}", files=files)
        else:
            res = requests.post(f"http://backend:8080/video/{style}", files=files)
        json = res.json()
        
        if "message" in json:
            st.error(json.get('message'), icon="🚨")

        if (filetype == 'Image'):
            image = Image.open(json.get('name'))
            st.image(image)
        else:
            st.video(json.get('name'))
        st.write("Size: {}".format(json.get('size')))