import pandas as pd

def explore_data(df):
    """Explora los datos con estadísticas básicas"""
    print("🔍 Información del dataset:")
    print(df.info())
    print("\n📊 Estadísticas descriptivas:")
    print(df.describe())
