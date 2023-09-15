from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion Stage"
try:
    logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<")
except Exception as e:
    logger.error(f"stage name: {STAGE_NAME} error: {e}")
    raise e