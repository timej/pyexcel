import pandas as pd

df = pd.read_excel('data/sample1.xlsx')
nd = df['顧客'].unique()
pd.Series(nd).to_clipboard()