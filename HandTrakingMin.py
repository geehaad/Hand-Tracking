import cv2
import mediapipe as mp
import time #to check the frame rate

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands() #Only uses RGB imgs
mpDraw = mp.solutions.drawing_utils #Helps us draw lines between the points on the hand

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Convert img to RGB
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks: #Check if the hand is detected or not
        for handLms in results.multi_hand_landmarks: #We have to check if we have multiple hands and extract it one by one
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
