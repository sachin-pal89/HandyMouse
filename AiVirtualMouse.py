import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

########################

wCam, hCam = 640, 480
frameR = 120  # Frame Reduction

########################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:

    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check which finger are up
        fingers = detector.fingersUp()
        # print(fingers)

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        # 4. Only index finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert our Coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # 6. Smoothen Values

            # 7. Move Mouse
            autopy.mouse.move(wScr - x3, y3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        # 8. Both Index and Middle Finger are up : Clicking Mode
        # 9. Find distance between fingers
        # 10. Click Mouse if distance short

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (15, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
