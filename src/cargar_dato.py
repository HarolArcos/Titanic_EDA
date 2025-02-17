import pandas as pd

# Carga el archivo CSV
df = pd.read_csv("../data/train_and_test2.csv")

# Visualizar las primeras filas
print(df.head())

# Ver la informacion del dataframe (tipos de datos y valores no nulos)
print(df.info())
