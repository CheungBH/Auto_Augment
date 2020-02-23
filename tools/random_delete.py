import os, random

folder = ""
ratio = 0.3    # If 0.3, 3 images will be deleted randomly in 10

img_ls = []
for root, dirs, files in os.walk(folder):
    path = [os.path.join(root, name) for name in files]
    img_ls.extend(path)
delete_ls = random.sample(img_ls, int(ratio * len(img_ls)))

for file in delete_ls:
    os.remove(file)
