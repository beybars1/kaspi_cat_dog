import pandas as pd

df = pd.read_json(r'C:\Users\user\PycharmProjects\kaspi_cat_dog\test\output.json')
df.to_csv(r'C:\Users\user\PycharmProjects\kaspi_cat_dog\test\test.csv', index=None, encoding='utf-8')
