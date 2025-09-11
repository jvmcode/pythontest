# Verificar Dimensões Inconsistentes das Imagens
import pandas as pd
from PIL import Image
import os
from collections import Counter

# Carrega o CSV
df = pd.read_csv('archive/sports.csv')

# Filtra imagens da classe 'football'
df_football = df[(df['labels'] == 'football') & (df['data set'] == 'train')]

# Lista para armazenar dimensões
dimensoes = []

for rel_path in df_football['filepaths']:
    full_path = os.path.join('archive', rel_path)
    try:
        with Image.open(full_path) as img:
            dimensoes.append(img.size)  # (largura, altura)
    except Exception as e:
        print(f"Erro ao abrir {full_path}: {e}")

# Verifica dimensões únicas
dim_set = set(dimensoes)
print(f"\n📏 Dimensões únicas encontradas: {dim_set}")

# Frequência das dimensões
dim_freq = Counter(dimensoes)
print("\n📊 Frequência das dimensões:")
for (w, h), count in dim_freq.items():
    print(f"{w}x{h}: {count} imagens")

"""
Como tratar:
Remover: df.dropna() elimina linhas com valores ausentes.

Preencher: df.fillna('desconhecido') substitui valores nulos por um valor padrão.

Investigar: Se muitos dados estiverem ausentes, pode indicar erro na coleta ou exportação.
"""