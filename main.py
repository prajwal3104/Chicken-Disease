from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_preppare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion Stage"
try:
    logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<")
except Exception as e:
    logger.error(f"stage name: {STAGE_NAME} error: {e}")
    raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<")
    except Exception as e:
        logger.error(f"stage name: {STAGE_NAME} error: {e}")
        raise e