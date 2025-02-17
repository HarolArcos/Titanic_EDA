# clean_data.py
import pandas as pd

# Cargar el dataset
df = pd.read_csv("../data/train_and_test2.csv")

# Verificar si hay valores nulos
print(df.isnull().sum())

# Eliminar duplicados
df = df.drop_duplicates()

# Llenar valores nulos con la media (en este caso para la columna 'Age', pero puedes cambiarla según lo necesites)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Si en caso se quisiera eliminar filas con valores nulos:
 #df = df.dropna()

# Guardar el dataframe limpio
df.to_csv('../data/titanic_clean.csv', index=False)
