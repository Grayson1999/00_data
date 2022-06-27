import pandas as pd


df = pd.read_excel("bert데이터셋/데이터 합침.xlsx")

df_shuffled=df.sample(frac=1).reset_index(drop=True)

df_shuffled.to_excel("shuffled_data.xlsx", index=False)