<H1 align="center">
Smart Traffic Control Using YOLOv8 Object Detection with DeepSORT Tracking </H1>

## Steps to run Code

- Go to the folder.
```
cd YOLOv8-DeepSORT-Object-Tracking
```
- Install the dependecies
```
pip install -e '.[dev]'
```
- Setting the Directory.
```
cd ultralytics/yolo/v8/detect
```
- Downloading the DeepSORT Files From The Google Drive 
```
https://drive.google.com/drive/folders/1kna8eWGrSfzaR6DtNJ8_GchGgPMv3VC8?usp=sharing
```
- After downloading the DeepSORT Zip file from the drive, unzip it go into the subfolders and place the deep_sort_pytorch folder into the yolo/v8/detect folder


- Run the code with mentioned command below.

- For yolov8 object detection + Tracking
```
 python predict.py model=yolov8l.pt source="demo1.mp4" show=True
