import pandas as pd

def clean_data(df):
    """Limpia los datos eliminando valores nulos y duplicados"""
    df_clean = df.dropna().drop_duplicates()
    return df_clean
