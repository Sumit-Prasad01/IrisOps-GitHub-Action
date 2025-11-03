from src.logger import get_logger
from src.custom_exception import CustomException
from src.data_processing import DataProcessing
from src.model_training import ModelTraining

logger = get_logger(__name__)

if __name__ == "__main__":

    try:

        logger.info("Training Pipeline Started.")

        # Data preprocessing
        data_processor = DataProcessing("artifacts/raw/data.csv")
        data_processor.run()

        logger.info("Data Proprocessing done.")

        logger.info("Model training started.")
        # Model Training
        trainer =  ModelTraining()
        trainer.run()

        logger.info("Model training completed successfully.")

    except Exception as e:
        logger.error(f"Error while data processing and model training. {e}")
        raise CustomException("Failed to process data and train model.", e)