import pandas as pd
import os
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(filepath=None):
    """Carga los datos desde un archivo CSV.
    
    Args:
        filepath (str, optional): Ruta del archivo CSV. Si es None, se usa el archivo original.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        if filepath is None:
            # Usar el dataset original si no se especifica una ruta
            filepath = os.path.join(os.path.dirname(__file__), "../data/train_and_test2.csv")
        
        filepath = os.path.abspath(filepath)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"❌ El archivo {filepath} no existe.")

        logger.info(f"📂 Cargando datos desde: {filepath}")
        return pd.read_csv(filepath)
    except FileNotFoundError as e:
        logger.error(e)
        return None
    except pd.errors.EmptyDataError:
        logger.error("El archivo está vacío.")
        return None
    except pd.errors.ParserError:
        logger.error("Error al parsear el archivo CSV.")
        return None
    except Exception as e:
        logger.error(f"Error inesperado al cargar los datos: {e}")
        return None