import os

folder = "../image/test_resize"
paths = [os.path.join(folder, name) for name in os.listdir(folder)]
for idx, img_path in enumerate(paths):
    os.rename(img_path, os.path.join(folder, "image_{}.jpg".format(idx)))
