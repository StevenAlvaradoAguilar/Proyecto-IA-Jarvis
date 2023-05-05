
    
import face_recognition
import cv2
import numpy as np

# Obtiene la referencia de la cámara
video_capture = cv2.VideoCapture(0)

# Cargamos imagenes de prueba para entrenar al modelo y sea capaz de reconocerlas
jordan_image = face_recognition.load_image_file("users/jordan.jpg")
jordan_image_encoding = face_recognition.face_encodings(jordan_image)[0]

steven_image = face_recognition.load_image_file("users/steven.jpg")
steven_image_encoding = face_recognition.face_encodings(steven_image)[0]

victor_image = face_recognition.load_image_file("users/victor.jpg")
victor_image_encoding = face_recognition.face_encodings(victor_image)[0]

# Se crea un arreglo con los códigos de las caras conocidas y con sus nombres
known_face_encodings = [
    jordan_image_encoding,
    steven_image_encoding,
    victor_image_encoding
]

known_face_names = [
    "Jordán",
    "Steven",
    "Victor"
]

# Inicialización de variables necesarias
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Se toma un solo frame del video
    ret, frame = video_capture.read()

    # Se redimenciona la imagen a un cuarto de su tamaño inicial para mayor facilidad en el porcesamiento
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)

    # Convertir la imagen de BGR (colores que utliza OpenCV) a RGB
    #rgb_small_frame = small_frame[:, :, ::-1]   
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    if process_this_frame:  
        # Encuentra todas las caras y caras codiicadas en el frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # OJO ACA, PUEDE QUE DEBA CAMBIARLO
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Se verifica si el rostro se iguala con alguno de los válidos
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Si sí hace match, entonces se debe abrir la opción de acceder a la IA de voz
                # Y a poder hacer preguntas a los modelos
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Mostrar los resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Dibujar una caja alrededor de la cara
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dibujar un texto con el nombre debajo de la cara
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Desplegar la imagen
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()