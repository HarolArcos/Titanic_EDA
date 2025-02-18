import pandas as pd
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_data(df, output_filepath=None):
    """Limpia los datos eliminando valores nulos, duplicados y columnas innecesarias.
    
    Args:
        df (pd.DataFrame): DataFrame original.
        output_filepath (str, optional): Ruta para guardar el archivo limpio. 

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    try:
        # Eliminar columnas que empiezan con 'zero'
        cols_to_drop = [col for col in df.columns if col.startswith("zero")]
        df_clean = df.drop(columns=cols_to_drop, errors="ignore")
        
        # Eliminar valores nulos y duplicados
        df_clean = df_clean.dropna().drop_duplicates()
        
        logger.info(f"🛠 Eliminadas {len(cols_to_drop)} columnas innecesarias.")
        
        # Si se especifica una ruta de salida, guardar el archivo limpio
        if output_filepath:
            df_clean.to_csv(output_filepath, index=False)
            logger.info(f"📂 Datos limpios guardados en: {output_filepath}")
        
        return df_clean
    except Exception as e:
        logger.error(f"Error al limpiar los datos: {e}")
        return None