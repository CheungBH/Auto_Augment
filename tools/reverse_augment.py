import os

folder = "../image/test_resize"
delete_type = "chnl"  #cut/cr/chnl

paths = []
for root, dirs, files in os.walk(folder):
    path = [os.path.join(root, name) for name in files]
    paths.extend(path)

for file in paths:
    if delete_type in file:
        os.remove(file)
