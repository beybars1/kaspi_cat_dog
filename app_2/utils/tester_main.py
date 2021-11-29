from torchvision import transforms
import torch
import time
from AnimalDataset import AnimalDataset
import requests
import json
from torchvision import models
from torch import nn
import warnings

warnings.filterwarnings("ignore")

test_transforms = transforms.Compose([transforms.Resize(255),
                                          transforms.CenterCrop(224),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0.485, 0.456, 0.406],
                                                               [0.229, 0.224, 0.225])])

json_file = open('test2.json')

dataset = {'predict': AnimalDataset(json_file, test_transforms)}
dataloader = {'predict': torch.utils.data.DataLoader(dataset['predict'], batch_size=1, shuffle=False, num_workers=0)}

json_file.close()

since = time.time()

for dict in dataloader['predict']:
    model_path = 'catvdog.pth'

    checkpoint = torch.load(model_path, map_location='cpu')

    model = models.densenet121(pretrained=False)
    model.classifier = nn.Sequential(nn.Linear(1024, 512),
                                     nn.ReLU(),
                                     nn.Dropout(0.2),
                                     nn.Linear(512, 256),
                                     nn.ReLU(),
                                     nn.Dropout(0.1),
                                     nn.Linear(256, 2),
                                     nn.LogSoftmax(dim=1))
    model.parameters = checkpoint['parameters']
    model.load_state_dict(checkpoint['state_dict'])

    model.eval()

    image = dict['image']
    #print(image)
    result = torch.exp(model(image))
    # print(result)

    np_result = result.detach().numpy()[0]
    # print(np_result)
    print("ID", dict['ID'][0])
    print("cat:", str(np_result[0]))
    print("dog:", str(np_result[1]))
    print("----------------------------------")
