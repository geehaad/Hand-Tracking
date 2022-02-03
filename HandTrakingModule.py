import cv2
import mediapipe as mp
import time #to check the frame rate

class handDetector():
    def __init__(self,mode=False, MaxHands = 2, detectionCon=0.5, trackCon=0.5):
                 self.mode = mode #object variable


mpHands = mp.solutions.hands
hands = mpHands.Hands() #Only uses RGB imgs
mpDraw = mp.solutions.drawing_utils #Helps us draw lines between the points on the hand


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Convert img to RGB
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks: #Check if the hand is detected or not
        for handLms in results.multi_hand_landmarks: #We have to check if we have multiple hands and extract it one by one
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id ==0: #ditect the bottom of the hand
                    cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255),3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)

def main():
    pTime = 0  # Previous time
    cTime = 0  # Current time

    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()