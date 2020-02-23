import cv2
import os

img_folder = "../image/test_resize"
dest_folder = img_folder + "_resize"
os.makedirs(dest_folder, exist_ok=True)

img_ls = [os.path.join(img_folder, img_name) for img_name in os.listdir(img_folder)]
dest_ls = [name.replace(img_folder, dest_folder) for name in img_ls]

for idx in range(len(img_ls)):
    img = cv2.imread(img_ls[idx])
    resize_img = cv2.resize(img, (540, 360))
    cv2.imwrite(dest_ls[idx], resize_img)
