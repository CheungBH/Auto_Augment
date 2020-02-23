import os
import shutil
import config.config as c


def folder_to_img(src_folder):
    folder_ls = [os.path.join(src_folder, name) for name in os.listdir(src_folder)]

    img_ls = []
    for root, dirs, files in os.walk(src_folder):
        path = [os.path.join(root, name) for name in files]
        img_ls.extend(path)

    for img in img_ls:
        shutil.move(img, src_folder)

    for folder in folder_ls:
        os.removedirs(folder)


if __name__ == '__main__':
    path = c.image_folder
    assert os.path.isdir(path), "Your directory is wrong!!"
    folder_to_img(path)
