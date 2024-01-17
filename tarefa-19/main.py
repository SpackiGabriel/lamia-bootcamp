import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print(cap)

while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color
    low_red = np.array([0, 48, 51])
    height_red = np.array([0, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, height_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Blue color
    low_blue = np.array([94, 82, 2])
    height_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, height_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # Green color
    low_green = np.array([25, 52, 72])
    height_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, height_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    # All colors except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    white = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("Frame", frame)
    #cv2.imshow("Red", red)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    cv2.imshow("Except white", white)
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break