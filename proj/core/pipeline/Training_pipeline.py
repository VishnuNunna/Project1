from core.components.Data_ingestion import DataIngestion
from core.components.Data_transformation import DataTransformation
from core.components.Model_trainer import ModelTrainer

obj=DataIngestion()
train_data,test_data=obj.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

modeltrainer=ModelTrainer()
print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
