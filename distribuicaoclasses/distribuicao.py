import pandas as pd
import matplotlib.pyplot as plt

# Carrega o CSV
df = pd.read_csv('archive/sports.csv')

# Filtra apenas o conjunto de treino
df_train = df[df['data set'] == 'train']

# Conta o número de imagens por classe
class_counts = df_train['labels'].value_counts()

# Exibe os valores
print("📊 Distribuição das classes no conjunto de treino:")
print(class_counts)

# Visualiza com gráfico de barras
plt.figure(figsize=(12,6))
class_counts.plot(kind='bar')
plt.title('Distribuição das Classes no Conjunto de Treino')
plt.xlabel('Classe')
plt.ylabel('Número de Imagens')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""
Como interpretar
Classes com muito mais imagens que outras podem dominar o aprendizado do modelo.

Classes com poucas imagens podem ser ignoradas ou mal classificadas.

Se houver diferença muito grande entre as classes, você pode considerar:

Amostragem balanceada (undersampling ou oversampling)

Pesos por classe no modelo

Data augmentation para classes minoritárias

"""