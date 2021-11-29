import base64
from io import BytesIO
from torch.utils.data import Dataset
import json
from PIL import Image


class AnimalDataset(Dataset):
    """Cat-Dog Dataset"""

    def __init__(self, json_file, transform=None):
        """
        Args:
            json_file: JSON input file with images' IDs and BASE64 encoded images
        """
        self.input_dict = json.load(json_file)
        self.transform = transform

    def __len__(self):
        return len(self.input_dict[next(iter(self.input_dict))])

    def __getitem__(self, idx):

        image_name = self.input_dict[next(iter(self.input_dict))][idx]["ID"]
        image_code = self.input_dict[next(iter(self.input_dict))][idx]["img_code"]
        base64_decoded = base64.b64decode(image_code)
        image = BytesIO(base64_decoded)
        image = Image.open(image)
        image = self.transform(image)

        sample = {"ID": image_name, "image": image}

        return sample
