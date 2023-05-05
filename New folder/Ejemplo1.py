import asyncio
import io
import os
import sys
import json
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

def get_face_client():
    # This key will serve all examples in this document.
    KEY = "42cecfd82c8d4769817f39fddd6f7a7e"
    # This endpoint will be used in all examples in this quickstart.
    ENDPOINT = "https://proyecto-1-ia.cognitiveservices.azure.com/"
    credential = CognitiveServicesCredentials(KEY) 
    return FaceClient(ENDPOINT, credential)
    
faceClient = get_face_client()
image_url = 'https://pbs.twimg.com/media/Er3sr4LXcAM9bFp.jpg'
urllib.request.urlretrieve(url, 'python.jpg')
img = Image.open('python.jpg')
attributes = ["age", "gender"] 
include_id = True
include_landmarks = True
detection_model=["detection_03"]
detected_faces = face_client.face.detect_with_url(url, include_id, include_landmarks, attributes, raw = True,)
detected_faces.response.json()
color="blue"
font = ImageFont.truetype("arial.ttf", 20)

if detected_faces is not None:
    draw = ImageDraw.Draw(img)
for currFace in 

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
img.show()
img.save('test.jpg')