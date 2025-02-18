import argparse
import logging
from src.load_data import load_data
from src.clean_data import clean_data
from src.eda import explore_data
from src.visualization import generate_visualizations

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Configuración de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Análisis Exploratorio de Datos del Titanic.")
    parser.add_argument("--input", default="data/train_and_test2.csv", help="Ruta del archivo de datos original.")
    parser.add_argument("--output", default="data/titanic_cleaned.csv", help="Ruta para guardar los datos limpios.")
    args = parser.parse_args()

    # 1️⃣ Cargar el dataset original
    df_original = load_data(args.input)
    if df_original is None:
        logger.error("🚨 No se pudo cargar el archivo original. Saliendo del programa.")
        return

    # 2️⃣ Limpiar los datos y guardarlos en un nuevo archivo
    df_clean = clean_data(df_original, args.output)
    if df_clean is None:
        logger.error("🚨 No se pudieron limpiar los datos. Saliendo del programa.")
        return

    # 3️⃣ Cargar el dataset limpio para análisis
    df = load_data(args.output)
    if df is None:
        logger.error("🚨 No se pudo cargar el archivo limpio. Saliendo del programa.")
        return

    # 4️⃣ Exploración estadística
    explore_data(df)

    # 5️⃣ Visualización de datos
    generate_visualizations(df)

if __name__ == "__main__":
    main()