# testing file. creates POST request to local host with following input file, saves output.file

import requests
import json

input_json = 'input.json'

resp = requests.post("http://127.0.0.1:5555/predict", files={'file': (input_json, open(input_json, 'rb'))})

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(resp.json(), f, ensure_ascii=False, indent=4)

print(resp)
