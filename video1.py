import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("window", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
