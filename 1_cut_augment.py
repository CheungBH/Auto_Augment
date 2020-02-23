from augment.cut import cut_image
import os
import random
import cv2
import config.config as c


class CutAugment:
    def __init__(self, folder):
        assert os.path.isdir(folder), "The target folder doesn't exist!!"
        self.img_ls = []
        for root, dirs, files in os.walk(folder):
            path = [os.path.join(root, name) for name in files]
            self.img_ls.extend(path)
        self.cut_param = [[(20, 10), (10, 5), (80, 20), (60, 15)],
                            [(20, 10), (10, 5), (30, 10), (140, 30)],
                          [(30, 10), (10, 5), (150, 20), (30, 10)]]

    def __cut_img(self, img_path, num, param):
        dest_path = img_path.replace(".", "_cut{}.".format(num))
        img = cv2.imread(img_path)
        cut_img = cut_image(img, bottom=param[0][0]+random.randint(-param[0][1], param[0][1]),
                            top=param[1][0]+random.randint(-param[1][1], param[1][1]),
                            left=param[2][0]+random.randint(-param[2][1], param[2][1]),
                            right=param[3][0]+random.randint(-param[3][1], param[3][1]))
        cv2.imwrite(dest_path, cut_img)

    def process(self):
        for img_path in self.img_ls:
            for idx in range(len(self.cut_param)):
                self.__cut_img(img_path, idx, self.cut_param[idx])


if __name__ == '__main__':
    folder_path = c.image_folder
    CA = CutAugment(folder_path)
    CA.process()




