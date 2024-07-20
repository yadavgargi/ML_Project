import os
import sys
from src.exception import CustomException
from src.logger import  logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass  #decorater
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact', "train.csv")
    test_data_path: str=os.path.join('artifact', "test.csv")
    raw_data_path: str=os.path.join('artifact', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Exported the dataset as panda dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # exist_ok = true if file is there then we will use existing one only instead of deleting and creating again
            df.to_csv (self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("data spliting  and injestion is done")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
            
        except Exception as e:
            raise CustomException (e, sys)
        

#initate and run this class

if __name__=="__main__":
    obj= DataIngestion()
    obj.initate_data_ingestion()









