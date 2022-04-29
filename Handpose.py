import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

mp_drawing = mp.solutions.drawing_utils #importing landmark model (draws landmarks)
mp_hands = mp.solutions.hands #importing hand model (finds landmarks)

from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS
cap = cv2.VideoCapture(0)

#setting up mediapipe with openCV
#ideal min-detection and min_tracking for handpose detection
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    ret, frame = cap.read()

    #Opencv takes BGR - need mediapipe to take in RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False 
    results = hands.process(image) #detection
    image.flags.writeable = True
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    #results.multi_hand_landmarks ==> strings of landmarks of recent frame

    #rendering ==> HAND_CONNECTIONS: standard connections between hand landmarks
    if results.multi_hand_landmarks:
      for num,hand in enumerate(results.multi_hand_landmarks):
        mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)) 



    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()  