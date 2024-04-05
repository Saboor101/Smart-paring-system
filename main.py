import cv2
import pickle
import cvzone
import numpy as np

# GUI Check availability





# Video feed
cap= cv2.VideoCapture('carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48


def checkParkingSpace(imgPro):

    slotlist = []
    spaceCounter = 0
    slotcounter = 0
    avail = []

    for pos in posList:

        slotcounter += 1
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        # print(imgCrop)
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            avail.append(1)
            spaceCounter += 1
            slotlist.append("slotNO-"+str(slotcounter))
        else:
            color = (0, 0, 255)
            thickness = 2
            avail.append(0)

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, "slot "+str(slotcounter), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free available slots: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))
    avail.append(spaceCounter)
    with open('Avail', 'wb') as f:
        pickle.dump(avail, f)

    slotstring=""
    for s in slotlist:
        slotstring+=" "+s                       
    # print(spaceCounter)
    # print(slotlist)
    # print(slotstring)

# root.mainloop()

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)

