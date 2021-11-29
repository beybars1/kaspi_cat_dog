# KASPI CAT-DOG End-to-End Project

![This is an image](https://images.ctfassets.net/82d3r48zq721/45liwTLsDMSJt4N22RqrHX/cd992f88ca8737f95b085212906d6d86/Can-cats-and-dogs-get-coronavirus_resized.jpg?w=800&q=50)

## About
This repository implements the inference of the deep learning classification model to classify images of dogs and cats via the Flask framework.
The classification model was taken from [Author](https://github.com/amitrajitbose),
author achieved 98% accuracy on validation set of famous Kaggle's Dogs vs. Cats [dataset](https://www.kaggle.com/c/dogs-vs-cats/data).
The neural network model architecture is based on the 121-layer DenseNet, implemented on PyTorch framework.

## Project Details
Project's main tasks
- Web scrape 500 images of cats and dogs for each class from the open-source ([image_web_scraper.py](https://github.com/beybars1/kaspi_cat_dog/blob/master/app_2/image_web_scraper.py))
- Convert retrieved 1000 images to the BASE64 format and store in the [input.json](https://github.com/beybars1/kaspi_cat_dog/blob/master/test/input.json)
as well as corresponding image names (aka **ID**)
- Prepare and configure the pretrained 121-layer DenseNet model with a custom classification layer via PyTorch
- Built a web-application via Flask framework
- Run the [test.py](https://github.com/beybars1/kaspi_cat_dog/blob/master/test/test.py) to get prediction results as
the [output.json](https://github.com/beybars1/kaspi_cat_dog/blob/master/test/output.json)
- Export results to the Excel and analyze the model performance

## Requirements
It is recommended to create python **virtual environment** and configure it with `pip install -r requirements.txt`
<details><summary>requirements.txt</summary>
<p>

      certifi==2021.10.8
      charset-normalizer==2.0.8
      click==8.0.3
      colorama==0.4.4
      cycler==0.11.0
      Flask==2.0.2
      fonttools==4.28.2
      idna==3.3
      imageio==2.12.0
      itsdangerous==2.0.1
      Jinja2==3.0.3
      jsonify==0.5
      kiwisolver==1.3.2
      MarkupSafe==2.0.1
      matplotlib==3.5.0
      networkx==2.6.3
      numpy==1.21.4
      packaging==21.3
      pandas==1.3.4
      Pillow==8.4.0
      pyparsing==3.0.6
      python-dateutil==2.8.2
      pytz==2021.3
      PyWavelets==1.2.0
      requests==2.26.0
      scikit-image==0.18.3
      scipy==1.7.3
      setuptools-scm==6.3.2
      six==1.16.0
      tifffile==2021.11.2
      tomli==1.2.2
      torch==1.10.0
      torchaudio==0.10.0
      torchvision==0.11.1
      typing_extensions==4.0.0
      urllib3==1.26.7
      Werkzeug==2.0.2

</p>
</details>

## Usage

###### REST API
Run server at localhost (**PORT**: 5555) with [api.py](https://github.com/beybars1/kaspi_cat_dog/blob/master/app_2/app.py) by:
```
python api.py
```

###### API Access
Run [test.py](https://github.com/beybars1/kaspi_cat_dog/blob/master/test/test.py) by:
```
python test.py
```
The resulting [output.json](https://github.com/beybars1/kaspi_cat_dog/blob/master/test/output.json) is located at
> kaspi_cat_dog/test/output.json

## Results
Based on the results achieved by testing model with a 1000-image dataset, following metrics were retrieved:
- Accuracy: 98.20%
- Precision: 99.00%
- Recall: 97.44%
> NOTICE: It is assumed for dog class to be '1' and for cat class to be '0' during metrics calculation

![image](https://github.com/beybars1/kaspi_cat_dog/blob/master/fig.png)
