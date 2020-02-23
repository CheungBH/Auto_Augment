import os

file_dir = "image/test1"
assert os.path.isdir(file_dir), "The target folder doesn't exist!!"
paths = []
for root, dirs, files in os.walk(file_dir):
    path = [os.path.join(root, name) for name in files]
    paths.extend(path)
print(paths)
