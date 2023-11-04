import os
import time
import cv2

base_dir = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\YOLO"


def capture_images(IMAGES_PATH):
    save_path = os.path.join(IMAGES_PATH, 'Data', 'new-imgs')
    number_images = 30
    cap = cv2.VideoCapture(0)
    i = 151
    for imgnum in range(number_images):
        print("Collecting image {}".format(imgnum + 1))
        ret, frame = cap.read()
        imgname = os.path.join(save_path, f"image{i}.jpg")
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame", frame)
        i += 1
        time.sleep(0.1)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    print("Images Captured!")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_images(base_dir)
