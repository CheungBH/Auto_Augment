import os
from augment.contrast_ratio import adjust_cr
import cv2
import random
import config.config as c


class ContrastRatioAugment:
    def __init__(self, folder):
        file = [os.path.join(folder, name) for name in os.listdir(folder)]
        assert os.path.isdir(file[0]), "No folder detected: Please make sure you have put the images into the folders!"
        self.img_ls = []
        for root, dirs, files in os.walk(folder):
            path = [os.path.join(root, name) for name in files]
            self.img_ls.extend(path)
        self.cr_param = [[(0.8, 0.05), (50, 20)],
                         [(1.4, 0.2), (30, 10)],
                         [(0.8, 0.05), (-20, 5)],
                         [(1.4, 0.2), (-50, 15)]]

    def process(self):
        for img_path in self.img_ls:
            print("\n\n")
            print("Processing img: {}".format(img_path))
            for idx in range(len(self.cr_param)):
                print("Processing img {}".format(idx))
                self.__adjust_cr(img_path, idx, self.cr_param[idx])

    def __adjust_cr(self, img_path, num, param):
        dest_path = img_path.replace(".", "_cr{}.".format(num))
        img = cv2.imread(img_path)
        cr_img = adjust_cr(img, alpha=param[0][0]+random.uniform(-abs(param[0][1]), abs(param[0][1])),
                            beta=param[1][0]+random.uniform(-abs(param[1][1]), abs(param[1][1])))
        cv2.imwrite(dest_path, cr_img)


if __name__ == '__main__':
    CRA = ContrastRatioAugment(c.image_folder)
    CRA.process()

