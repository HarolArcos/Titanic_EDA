import pandas as pd
import os

def load_data():
    """Carga los datos desde el CSV ubicado en la carpeta 'data'"""
    filepath = os.path.join(os.path.dirname(__file__), "../data/train_and_test2.csv")
    filepath = os.path.abspath(filepath)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ El archivo {filepath} no existe.")

    return pd.read_csv(filepath)
