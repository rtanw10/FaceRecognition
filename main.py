import cv2
import time

def main():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise IOError("Error: Cannot Open Webcam")

    while True:
        ret, frame = camera.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        if (cv2.waitKey(1) == 27):
            break

        cv2.imshow("Checking Face...", frame)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()