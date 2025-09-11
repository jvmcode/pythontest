# Verificar Valores Ausentes nos Metadados

import pandas as pd

# Carrega o CSV
df = pd.read_csv('archive/sports.csv')

# Verifica valores ausentes por coluna
missing_values = df.isnull().sum()

print("🔍 Valores ausentes por coluna:")
print(missing_values)

# Exibe linhas com qualquer valor ausente
rows_with_missing = df[df.isnull().any(axis=1)]
print(f"\n❌ Total de linhas com valores ausentes: {len(rows_with_missing)}")
print(rows_with_missing)
