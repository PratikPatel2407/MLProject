import pandas as pd
import sys
from src.components import data_transformation
from src.exception import CustomException
from src.logger import logging
import os

from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from sklearn.model_selection import train_test_split

from src.components.model_trainer import ModelTrainer,ModelTrainerConfig





class DataIngestionConfig:
    train_data_path: str =os.path.join('artifacts', 'train.csv')
    test_data_path: str =os.path.join('artifacts', 'test.csv')
    raw_data_path: str= os.path.join('artifacts', 'data.csv')


class DataIngestion:
   def __init__(self):
      self.ingetion_config =DataIngestionConfig()
      
   def initiate_data_ingestion(self):
       
       logging.info("Entered the data ingestion method or component")
         
       try: 
           df = pd.read_csv(r'C:/desktop/mlproject/notebook/data/data.csv')
          
           logging.info('read the dataset as dataframe')
           
           os.makedirs(os.path.dirname(self.ingetion_config.train_data_path), exist_ok=True)
           df.to_csv(self.ingetion_config.raw_data_path, index=False, header=True)

           logging.info('Train test split intiated')
           train_set, test_set =train_test_split(df, test_size=0.2, random_state=42)

           train_set.to_csv(self.ingetion_config.train_data_path, index =False, header =True)

           test_set.to_csv(self.ingetion_config.test_data_path, index=False, header =True)
            
           logging.info('ingestion of data is completed')

           return(self.ingetion_config.train_data_path,self.ingetion_config.test_data_path) 

       except Exception as e:
           raise CustomException(e, sys)
           

        

if __name__== '__main__':
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
 
    data_trasformation = DataTransformation()
    train_arr,test_arr,_=data_trasformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))