import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object 
import pandas as pd


class Predictionpipeline:
    def __ini__(self):
        pass
    def predict(self,features):
        try:
            logging.info('start predict ')
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')
            logging.info('Load preprocessor.pkl  with preprocessor_path=',preprocessor_path)
            preprocessor=load_object(preprocessor_path)
            logging.info('Load model.pkl  with model_path=',model_path)
            model=load_object(model_path)
            logging.info('transform feautures')
            data_scaled=preprocessor.transform(features)
            logging.info('Predict')
            pred=model.predict(data_scaled)
            logging.info('Return prediction ')
            return pred
        except Exception as e:
            logging.info('Exception occured in Prediction')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(seld,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:float,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut=cut
        self.color=color
        self.clarity=clarity

    def  get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                 'x':[self.x],
                 'y':[self.y],
                 'cut':[self.cut],
                  'color':[self.color],
                  'clarity':[self.clarity]
            }
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('Data Frame gathered')
            return df
        except Exception as e:
            logging.info('Exception occured prediction pipeline')
            raise CustomException(e,sys)
            
            
            
            
            



