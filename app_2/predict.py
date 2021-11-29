from utils.helpers import *
from torchvision import transforms
from utils.AnimalDataset import *
from utils.helpers import load_model

test_transforms = transforms.Compose([transforms.Resize(255),
                                      transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])])


def predict(json_file):

    dataset = {'predict': AnimalDataset(json_file, test_transforms)}
    dataloader = {'predict': torch.utils.data.DataLoader(dataset['predict'], batch_size=1, shuffle=False, num_workers=0)}

    result_dict = {"results": []}

    for i, batched_dict in enumerate(dataloader['predict']):

        model_path = './app_2/utils/catvdog.pth'
        #model_path = 'catvdog.pth'
        model = load_model(model_path)
        model.eval()

        image = batched_dict['image']
        result = torch.exp(model(image))

        np_result = result.detach().numpy()[0]
        result_dict["results"].append({'ID': batched_dict['ID'][0],
                                       'cat_prob': str(round(np_result[0], 3)),
                                       'dog_prob': str(round(np_result[1], 3))})

    return result_dict
