import pandas as pd

def clean_data(df):
    """Limpia los datos eliminando valores nulos, duplicados y columnas innecesarias."""
    
    # Eliminar columnas que empiezan con 'zero'
    cols_to_drop = [col for col in df.columns if col.startswith("zero")]
    df_clean = df.drop(columns=cols_to_drop, errors="ignore")
    
    # Eliminar valores nulos y duplicados
    df_clean = df_clean.dropna().drop_duplicates()
    
    print(f"🛠 Eliminadas {len(cols_to_drop)} columnas innecesarias.")
    
    return df_clean
