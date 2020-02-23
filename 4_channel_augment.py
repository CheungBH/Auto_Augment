import os
import cv2
import random
import config.config as c

mode = "replace"    # the src file will be deleted if mode="replace"
ratio = 0.3


class ChannelAugment:
    def __init__(self, folder):
        file = [os.path.join(folder, name) for name in os.listdir(folder)]
        assert os.path.isdir(file[0]), "No folder detected: Please make sure you have put the images into the folders!"
        img_ls = []
        for root, dirs, files in os.walk(folder):
            path = [os.path.join(root, name) for name in files]
            img_ls.extend(path)
        self.img_ls = random.sample(img_ls, int(ratio*len(img_ls)))
        self.mode = mode

    def process(self):
        for img_path in self.img_ls:
            self.__adjust_channel(img_path)

    def __adjust_channel(self, img_path):
        dest_path = img_path.replace(".", "_chnl.")
        img = cv2.imread(img_path)
        res = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(dest_path, res)
        if self.mode == "replace":
            os.remove(img_path)


if __name__ == '__main__':
    CRA = ChannelAugment(c.image_folder)
    CRA.process()
