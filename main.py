import pandas as pd

df = df = pd.read_csv('archive/sports.csv')

df_train = df[df['data set'] == 'train']

contagem = df_train['labels'].value_counts()

print("Top 10 classes com mais imagens:")
print(contagem.head(10))