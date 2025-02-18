import pandas as pd
import os

def load_data(filepath=None):
    """Carga los datos desde un archivo CSV.
    
    Args:
        filepath (str, optional): Ruta del archivo CSV. Si es None, se usa el archivo original.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    if filepath is None:
        # Usar el dataset original si no se especifica una ruta
        filepath = os.path.join(os.path.dirname(__file__), "../data/train_and_test2.csv")
    
    filepath = os.path.abspath(filepath)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ El archivo {filepath} no existe.")

    print(f"📂 Cargando datos desde: {filepath}")
    return pd.read_csv(filepath)
