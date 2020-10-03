import pandas as pd

df = pd.read_csv("https://api-tokyochallenge.odpt.org/api/v4/files/KDDI/data/KLD100101_1.csv?acl:consumerKey=1IjL7T3KYjAlJ5GIbxcUYtnbE4nYF3FLTtMs9aRq404")
print(df.head())