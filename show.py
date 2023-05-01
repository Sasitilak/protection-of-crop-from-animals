from ultralytics import YOLO
from PIL import Image

import cv2
import os
import sys
model = YOLO("yolov8n.pt")
results = model.predict(source= "0", show=True) 
im2 = cv2.imread("0")
results = model.predict(source=im2, save=True, save_txt=True)  