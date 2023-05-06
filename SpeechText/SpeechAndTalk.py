import speech_recognition as sr
from gtts import gTTS
import playsound
import os
# Función para que el bot escuche
def jackie_Escucha():
    r = sr.Recognizer()
    print("Escuchando ...")
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ''
        try: 
            text = r.recognize_google(audio,language= "es")
        except sr.RequestError as rs:
            print(rs)
        except sr.UnknownValueError as uve:
            print(uve)
        except sr.WaitTimeOutError as wte:
            print(wte)
    text = text.lower()
    return text
# Función del bot para hablar
def Jackie_Habla(text):
    file_name = 'audio_data.mp3'
    tts = gTTS(text = text,lang = 'es')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)