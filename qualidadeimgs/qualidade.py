# Qualidade das Imagens
# img.verify() é usado para validar a integridade da imagem sem carregá-la completamente.
# Se a imagem estiver corrompida, o verify() vai lançar uma exceção que você captura com except.

from PIL import Image
import pandas as pd
import os

# Carrega o CSV
df = pd.read_csv('archive/sports.csv')

# Filtra imagens da classe 'football' no conjunto de treino
df_football = df[(df['labels'] == 'football') & (df['data set'] == 'train')]

# Lista para armazenar imagens corrompidas
corrompidas = []

# Verifica cada imagem
for rel_path in df_football['filepaths']:
    full_path = os.path.join('archive', rel_path)
    try:
        with Image.open(full_path) as img:
            img.verify()  # Verifica se a imagem pode ser carregada
    except Exception as e:
        corrompidas.append(full_path)
        print(f"❌ Imagem corrompida: {full_path} — Erro: {e}")

# Resultado final
print(f"\n🔍 Total de imagens corrompidas encontradas: {len(corrompidas)}")
