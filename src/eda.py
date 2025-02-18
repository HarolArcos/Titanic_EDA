import pandas as pd
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def explore_data(df):
    """Explora los datos con estadísticas básicas"""
    try:
        logger.info("🔍 Información del dataset:")
        logger.info(df.info())
        logger.info("\n📊 Estadísticas descriptivas:")
        logger.info(df.describe())
    except Exception as e:
        logger.error(f"Error al explorar los datos: {e}")