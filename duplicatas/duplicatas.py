#Verificar duplicatas

#Para detectar imagens duplicadas visualmente (mesmo conteúdo), você pode usar hashing perceptual. 
#Uma técnica comum é o hash de média (average hash) com a biblioteca imagehash.

import pandas as pd
import os
from PIL import Image
import imagehash

# Carrega o CSV
df = pd.read_csv('archive/sports.csv')

# Filtra imagens da classe 'football'
df_football = df[(df['labels'] == 'football') & (df['data set'] == 'train')]

# Dicionário para armazenar hashes
hash_dict = {}

# Verifica duplicatas visuais
for rel_path in df_football['filepaths']:
    full_path = os.path.join('archive', rel_path)
    try:
        with Image.open(full_path) as img:
            hash_val = str(imagehash.average_hash(img))
            if hash_val in hash_dict:
                hash_dict[hash_val].append(full_path)
            else:
                hash_dict[hash_val] = [full_path]
    except Exception as e:
        print(f"Erro ao abrir {full_path}: {e}")

# Exibe duplicatas
print("\n🔍 Imagens duplicadas visualmente:")
for hash_val, files in hash_dict.items():
    if len(files) > 1:
        print(f"\nHash: {hash_val}")
        for f in files:
            print(f" - {f}")
            
# Verifica duplicatas exatas
duplicatas = df[df.duplicated(subset=['filepaths'], keep=False)]

print(f"\n📄 Total de duplicatas no CSV: {len(duplicatas)}")
if not duplicatas.empty:
    print("\n🔁 Linhas duplicadas:")
    print(duplicatas)

