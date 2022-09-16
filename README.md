## Object Detection Web APP

### Tools
- FastAPI: for the API
- streamlit : for the interface
- Docker: to containerize the app


### Steps

#### Download the models
```bash
./download_models.sh
```

#### Run
```bash
docker-compose up -d
```
navigate to http://localhost:8501:

![!web detection sample video](./doc/img/web_detect_sample.gif)


### Reference
- [web app](https://testdriven.io/blog/fastapi-streamlit/)
- object detection 
    - [OpenCV-dnn](https://github.com/hpc203/yolov7-opencv-onnxrun-cpp-py)
    - [ONNXRuntime](https://github.com/ibaiGorordo/ONNX-YOLOv7-Object-Detection)
- [yolov7 onnx](https://github.com/PINTO0309/PINTO_model_zoo/tree/main/307_YOLOv7) 
- [download google drive files with wget](https://www.matthuisman.nz/2019/01/download-google-drive-files-wget-curl.html)