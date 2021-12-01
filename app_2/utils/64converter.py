# converts images to the BASE64 format and creates an "input.json" file with IDs and image codes.

import base64
import os
import json

path = 'C:\\Users\\user\\PycharmProjects\\kaspi_cat_dog\\data\\data_mixed\\'
files = os.listdir(path)

encoded_dict = {"photos": []}

for index, file in enumerate(files):
    path_file = os.path.join(path, file)
    with open(path_file, "rb") as img_file:
        img_encoded = (base64.b64encode(img_file.read())).decode('utf-8')
        encoded_dict["photos"].append({'ID': os.path.splitext(file)[0],
                                       'img_code': str(img_encoded)})
    img_file.close()

with open('input.json', 'w', encoding='utf-8') as f:
    json.dump(encoded_dict, f, ensure_ascii=False, indent=4)
f.close()
