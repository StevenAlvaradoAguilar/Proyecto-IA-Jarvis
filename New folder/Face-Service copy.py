import asyncio
import io
import os
import sys
import json
import time
import uuid
# import request
import urllib3
import urllib.parse
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
    
face_client = get_face_client()
image_url = 'https://pbs.twimg.com/media/Er3sr4LXcAM9bFp.jpg'
urllib.request.urlretrieve(urlparse, 'python.jpg')
img = Image.open('python.jpg')
attributes = ["age", "gender"] 
include_id = True
include_landmarks = True
detection_model=["detection_03"]
detected_faces = face_client.face.detect_with_url(urlparse, include_id, include_landmarks, attributes, raw = True,)
detected_faces.response.json()
color = "blue"
font = ImageFont.truetype("arial.ttf", 20)

if detected_faces is not None:
    draw = ImageDraw.Draw(img)
for currFace in detected_faces.response.json():
    faceRectangle = currFace['faceRectabgle']
    left = faceRectangle['left']
    top = faceRectangle['top']
    width = faceRectangle['width']
    height = faceRectangle['height']
    draw.line([(left, top), (left + width, top)], fill = color, width = 5)
    draw.line([(left + width, top), (left + width, top + height)], fill = color, width = 5)
    draw.line([(left + width, top + height), (left, top + height)], fill = color, width = 5)
    draw.line([(left, top + height), (left, top)], fill = color, width = 5)
    text = currFace['faceAttributes']['age']
    genero = currFace['faceAttributes']['gender']
    if str(genero) == 'male':
        genero = 'Masculino'
    else:
        genero = 'Femenino'
    draw.text((left, top + height), text= str('Edad: ' + str(text) + '\n' + 'Género: ' + genero))
img.show()