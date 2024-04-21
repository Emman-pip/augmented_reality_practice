import cv2 as cv

image = cv.imread("Untitled.png")
cv.imshow("Diagram", image)

cv.waitKey(0)
cv.destroyAllWindows()
