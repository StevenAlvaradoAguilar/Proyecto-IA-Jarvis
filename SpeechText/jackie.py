import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import openai
from usarModelos import * 
import re
from SpeechAndTalk import *
#Credenciales de chatGPT
openai.api_key = "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"
messages = [
    {"role": "system", "content": "You are gonna be a kind virtual assistant named jackie"},
     {"role": "system", "content": "talk only in spanish from now on"},
]
from funcionesJackie import *


#Función del robot para responder
def Jackie_Responde(text):
    messages.append(
            {"role": "user", "content": text},
        )
    if "what" in text and "name" in text:
        Jackie_Habla('Hi, my name is Jackie, and i am a virtual assistant, how can i help you')
    elif ("predicen" in text or "predice" in text or  "prediceme" in text or  "predigas" in text) and  "precio" in text and  "aguacate" in text:
        AvocadoPrediction()
    elif ("predicen" in text or "predice" in text or  "prediceme" in text or  "predigas" in text) and "vino" in text and "calidad" in text:
        WinePrediction()
    elif ("predicen" in text or "predice" in text or  "prediceme" in text or  "predigas" in text) and "hepatitis" in text and "tipo" in text:
        HepatitisPrediction()
    elif ("predicen" in text or "predice" in text or  "prediceme" in text or  "predigas" in text) and "cirrosis" in text and "tipo" in text:
        Jackie_Habla("Estoy prediciendo el tipo de cirrosis")
    elif ("predicen" in text or "predice" in text or  "prediceme" in text or  "predigas" in text)  and "accidente" in text and "cerebrovascular" in text:
        StrokePrediction()
    elif 'stop' in text :
        Jackie_Habla("Fue un placer hablar contigo")
    else:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print("Jackie: ", reply)
        Jackie_Habla(reply)
    return
def EjecutarJackie():
    Jackie_Habla('hola como estas')
    while True: 
        escucha = jackie_Escucha()
        print(escucha)
        if escucha:
            Jackie_Responde(escucha)
        if "para" in escucha:
            break
EjecutarJackie()