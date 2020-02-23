import os
import shutil
import config.config as c


def move_img_into_folder(img_folder):
    img_ls, folder_ls, dest_ls = [], [], []
    for name in os.listdir(img_folder):
        img_ls.append(os.path.join(img_folder, name))
        folder_ls.append(name.split(".")[0])
        dest_ls.append(os.path.join(img_folder, name.split(".")[0], name))
    
    assert len(set(folder_ls)) == len(img_ls), "Some images have the same name! (The format is different)"
    
    for idx in range(len(folder_ls)):
        os.makedirs(os.path.join(img_folder, folder_ls[idx]),exist_ok=True)
        shutil.move(img_ls[idx], dest_ls[idx])


if __name__ == '__main__':
    folder = c.image_folder
    move_img_into_folder(folder)
