import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def plot_age_distribution(df):
    """Visualiza la distribución de edades con un histograma y boxplot."""
    try:
        if 'Age' not in df.columns:
            logger.error("La columna 'Age' no existe en el DataFrame.")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        sns.histplot(df['Age'], bins=30, kde=True, ax=axes[0])
        axes[0].set_title("Distribución de Edades")
        
        sns.boxplot(x=df['Age'], ax=axes[1])
        axes[1].set_title("Boxplot de Edad")
        
        plt.show()
        plt.close()
    except Exception as e:
        logger.error(f"Error al graficar la distribución de edades: {e}")

def plot_survival_by_class_and_gender(df):
    """Muestra la cantidad de sobrevivientes según clase y género."""
    try:
        if 'Pclass' not in df.columns or 'Sex' not in df.columns:
            logger.error("Las columnas 'Pclass' o 'Sex' no existen en el DataFrame.")
            return
        
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x='Pclass', hue='Sex')
        plt.title("Supervivencia por Clase y Género")
        plt.show()
        plt.close()
    except Exception as e:
        logger.error(f"Error al graficar la supervivencia por clase y género: {e}")

def plot_correlation_heatmap(df):
    """Genera un mapa de calor de correlaciones entre variables numéricas."""
    try:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Mapa de Calor de Correlaciones")
        plt.show()
        plt.close()
    except Exception as e:
        logger.error(f"Error al generar el mapa de calor de correlaciones: {e}")

def generate_visualizations(df):
    """Genera todas las visualizaciones."""
    plot_age_distribution(df)
    plot_survival_by_class_and_gender(df)
    plot_correlation_heatmap(df)