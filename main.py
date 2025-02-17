from src.load_data import load_data
from src.clean_data import clean_data
from src.eda import explore_data

def main():
    print("🚀 Cargando datos...")
    df = load_data()
    print("✅ Datos cargados con éxito!\n")

    print("🛠 Limpiando datos...")
    df_clean = clean_data(df)
    print("✅ Datos limpiados con éxito!\n")

    print("📊 Exploración de datos...")
    explore_data(df_clean)
    print("🎉 Análisis completado!")

if __name__ == "__main__":
    main()
