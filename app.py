from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
#from src.mlproject.components.data_ingestion import DataIngestion
#from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

if __name__=="__main__":
    logging.info("The executionhas started")


    try:
       D=DataIngestionConfig()
       d=DataIngestion()
       train_data_path,test_data_path=d.initiate_data_ingestion()
       data_transformation_config=DataTransformationConfig()
       data_transformation=DataTransformation()
       data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        logging.info(CustomException)
        raise CustomException(e,sys)
   