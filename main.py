from src.load_data import load_data
from src.clean_data import clean_data
from src.eda import explore_data
from src.visualization import generate_visualizations

def main():
    # 1️⃣ Cargar el dataset original
    df_original = load_data("data/train_and_test2.csv")

    if df_original is None:
        print("🚨 No se pudo cargar el archivo original. Saliendo del programa.")
        return

    # 2️⃣ Limpiar los datos y guardarlos en un nuevo archivo
    cleaned_filepath = "data/titanic_cleaned.csv"
    df_clean = clean_data(df_original, cleaned_filepath)

    # 3️⃣ Cargar el dataset limpio para análisis
    df = load_data(cleaned_filepath)

    # 4️⃣ Exploración estadística
    explore_data(df)

    # 5️⃣ Visualización de datos
    generate_visualizations(df)

if __name__ == "__main__":
    main()
