# renames images with "1, 2, 3, ... 1000".

import os
path = 'C:\\Users\\user\\PycharmProjects\\kaspi_cat_dog\\data\\cat'
files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(501+index), '.jpg'])))
