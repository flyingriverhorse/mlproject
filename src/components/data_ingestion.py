import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #decorator to automatically generate special methods like __init__ and __repr__
class DataIngestionConfig:
    #creating the config for data ingestion 
    #artifacts is a folder where we will save the data
    #train.csv is the file where we will save the training data
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    #test.csv is the file where we will save the testing data
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    #raw.csv is the file where we will save the raw data
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #creating the config object that will save 3 objects

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        #if any error comes
        try:
            #reading the data from the csv file
            file_path = 'notebook\data\stud.csv'
            #file_path = os.path.join('notebook', 'data', 'stud.csv')
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist. Please check the path.")
            df = pd.read_csv(file_path)  # Ensure the file exists at this path
            logging.info("Read the dataset as dataframe")

            #creating the directory for artifacts if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            #saving the raw data to the raw_data_path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")

            #splitting the data into training and testing data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) 

            #saving the training data to the train_data_path
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            #saving the testing data to the test_data_path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")
            
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys) from e

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion() #calling the function to initiate data ingestion
#This will run the code when this file is run directly