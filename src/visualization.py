import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """Visualiza la distribución de edades con un histograma y boxplot."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.histplot(df['Age'], bins=30, kde=True, ax=axes[0])
    axes[0].set_title("Distribución de Edades")
    
    sns.boxplot(x=df['Age'], ax=axes[1])
    axes[1].set_title("Boxplot de Edad")
    
    plt.show()

def plot_survival_by_class_and_gender(df):
    """Muestra la cantidad de sobrevivientes según clase y género."""
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Pclass', hue='Sex')
    plt.title("Supervivencia por Clase y Género")
    plt.show()

def plot_correlation_heatmap(df):
    """Genera un mapa de calor de correlaciones entre variables numéricas."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Calor de Correlaciones")
    plt.show()

# Función para llamar a todas las visualizaciones
def generate_visualizations(df):
    plot_age_distribution(df)
    plot_survival_by_class_and_gender(df)
    plot_correlation_heatmap(df)
