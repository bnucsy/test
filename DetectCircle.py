import cv2
import numpy as np

# read image
image = cv2.imread(r'C:\Users\cnbnu\Desktop\can.jpg')

# convert to gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, 
                           cv2.HOUGH_GRADIENT, 
                           dp=1, 
                           minDist=100, 
                           param1=100, 
                           param2=100, 
                           minRadius=90, 
                           maxRadius=250)
print(circles.shape)
# overlay circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# save image
cv2.imwrite(r'C:\Users\cnbnu\Desktop\can_circle.jpg', image)