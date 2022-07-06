import pandas as pd

df = pd.read_csv('file.csv', encoding='utf-8-sig')
df.drop(df[df['薪资'].str.contains('天')].index, inplace=True)

df.to_csv('file.csv', index=False, encoding='utf-8-sig')