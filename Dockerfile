FROM python:3.9

WORKDIR /kaspi_cat_dog

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app_2 ./app_2

COPY ./test ./test

CMD ["python", "./app_2/app.py"]