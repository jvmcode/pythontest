import pandas as pd
import os

# Caminho para o CSV e diretório de imagens
csv_path = 'archive/sports.csv'
image_root = 'archive/train/football'

# Lê o CSV
df = pd.read_csv(csv_path)

# Filtra apenas imagens da classe 'football' no conjunto de treino
df_football = df[(df['labels'] == 'football') & (df['data set'] == 'train')]

# Lista de caminhos esperados (relativos)
csv_files = df_football['filepaths'].tolist()

# Verifica se os arquivos listados no CSV existem no diretório
missing_files = []
wrong_format = []
expected_format = '.jpg'  # ou '.jpeg', '.png', dependendo do seu padrão

for rel_path in csv_files:
    full_path = os.path.join('archive', rel_path)
    if not os.path.isfile(full_path):
        missing_files.append(full_path)
    else:
        _, ext = os.path.splitext(full_path)
        if ext.lower() != expected_format:
            wrong_format.append(full_path)

# Verifica se há arquivos no diretório que não estão no CSV
dir_files = os.listdir(image_root)
csv_filenames = [os.path.basename(path) for path in csv_files]
extra_files = [file for file in dir_files if file not in csv_filenames]


# Resultados
print(f"🔍 Total de imagens listadas no CSV: {len(csv_files)}")
print(f"❌ Imagens listadas no CSV que não existem: {len(missing_files)}")
print(f"📁 Imagens no diretório que não estão no CSV: {len(extra_files)}")
print(f"🖼️ Imagens com formato diferente de {expected_format}: {len(wrong_format)}")

"""
🔄 Em resumo:
O código está fazendo uma verificação cruzada:

O que o CSV diz que deveria existir ✅

O que realmente existe na pasta ✅

Assim, você garante que o conjunto de dados está completo, organizado e sem erros
"""

















"""
# Exibir detalhes se quiser
if missing_files:
    print("\nArquivos ausentes:")
    for f in missing_files:
        print(f)

if extra_files:
    print("\nArquivos extras no diretório:")
    for f in extra_files:
        print(f)

if wrong_format:
    print("\nArquivos com formato incorreto:")
    for f in wrong_format:
        print(f)
"""