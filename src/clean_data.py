import pandas as pd

def clean_data(df, output_filepath=None):
    """Limpia los datos eliminando valores nulos, duplicados y columnas innecesarias.
    
    Args:
        df (pd.DataFrame): DataFrame original.
        output_filepath (str, optional): Ruta para guardar el archivo limpio. 

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    
    # Eliminar columnas que empiezan con 'zero'
    cols_to_drop = [col for col in df.columns if col.startswith("zero")]
    df_clean = df.drop(columns=cols_to_drop, errors="ignore")
    
    # Eliminar valores nulos y duplicados
    df_clean = df_clean.dropna().drop_duplicates()
    
    print(f"🛠 Eliminadas {len(cols_to_drop)} columnas innecesarias.")
    
    # Si se especifica una ruta de salida, guardar el archivo limpio
    if output_filepath:
        df_clean.to_csv(output_filepath, index=False)
        print(f"📂 Datos limpios guardados en: {output_filepath}")
    
    return df_clean
