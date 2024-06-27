import cv2
import numpy as np

def pipe_detection_algo(gray_img):
    # Convert the grayscale image to BGR for displaying results with colored circles
    output = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    imgBlur = cv2.GaussianBlur(gray_img, (7, 7), 1)

    # Apply the Hough Circle Transform algorithm to find circles in the blurred image
    circles = cv2.HoughCircles(imgBlur, cv2.HOUGH_GRADIENT, dp=1, minDist=22,
                               param1=50, param2=30, minRadius=11, maxRadius=25)

    count = 0
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Draw the circles on the output image
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)  # Circle outline
            cv2.circle(output, (x, y), 2, (0, 128, 255), 3)  # Circle center
            count += 1
    return output, count
