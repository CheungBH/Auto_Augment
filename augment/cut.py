import numpy as np
import cv2


def cut_image(img, bottom=0, top=0, left=0, right=0):
    height, width = img.shape[0], img.shape[1]
    return np.asarray(img[top: height - bottom, left: width - right])


if __name__ == '__main__':
    img_path = "../../img/err.jpg"
    saved_path = img_path.replace(".jpg", "_cut.jpg")
    img = cv2.imread(img_path)
    cut_img = cut_image(img, top=100)
    cv2.imwrite(saved_path, cut_img)
    cv2.imshow("cut", cut_img)
    cv2.waitKey(0)
