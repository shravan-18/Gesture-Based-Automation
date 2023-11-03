import os
import time
import uuid
import cv2

base_dir = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\OpenCV"


def capture_images(IMAGES_PATH):
    save_path = os.path.join(IMAGES_PATH, 'images', 'p')
    number_images = 100
    cap = cv2.VideoCapture(0)
    for imgnum in range(number_images):
        print("Collecting image {}".format(imgnum + 1))
        ret, frame = cap.read()
        imgname = os.path.join(save_path, f"{str(uuid.uuid1())}.jpg")
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame", frame)
        time.sleep(0.1)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    print("Images Captured!")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_images(base_dir)
