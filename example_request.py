# YOLOv5 🚀 by Ultralytics, AGPL-3.0 license
"""Perform test request."""

import pprint

import requests

DETECTION_URL = "http://172.17.0.2:5000/v1/object-detection/yolov5s"
IMAGE = "giang.jpg"

# Read image
with open(IMAGE, "rb") as f:
    image_data = f.read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

pprint.pprint(response)
