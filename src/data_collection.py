import pandas as pd 
from sklearn.model_selection import train_test_split
import os 
import yaml 

#test_size = yaml.safe_load(open('params.yaml'))['data_collection']['test_size']

def load_params(filepath: str) -> float:
    try:
        with open(filepath,'r') as file: 
            params = yaml.safe_load(file)
        return params['data_collection']['test_size']
    except Exception as e:
        raise(Exception(f"Error loading parameters from filepath {filepath}: {e}"))
    
#df = pd.read_csv(r"C:\Users\micahdel\Downloads\water_potability.csv")
def load_data(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise(Exception(f"Error loading data from filepath {filepath}:{e}"))
    
#train, test = train_test_split(df, test_size= test_size, random_state= 42)

def split_data(data:pd.DataFrame, test_size:float) -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        return train_test_split(data, test_size = test_size, random_state= 42 )
    except ValueError as e:
        raise ValueError(f"Error splitting data: {e}")
    
def save_data(data: pd.DataFrame, filepath: str) -> None:
    try:
        data.to_csv(filepath, index = False)
    except Exception as e:
        raise(Exception(f"Error saving data to {filepath}: {e}"))
    
def main():
    try:
        data_filepath = r"C:\Users\micahdel\Downloads\water_potability.csv"
        params_filepath = "params.yaml"
        raw_data_path = os.path.join("data","raw")
        #data_path = os.path.join("data","raw")
        # train.to_csv(os.path.join(data_path,'train.csv'), index = False)
        # test.to_csv(os.path.join(data_path,'test.csv'), index = False)
        data = load_data(data_filepath)
        test_size = load_params(params_filepath)
        train_data, test_data = split_data(data, test_size)
        os.makedirs(raw_data_path)
        save_data(train_data, os.path.join(raw_data_path,'train.csv'))
        save_data(test_data, os.path.join(raw_data_path,'test.csv'))

    except Exception as  e: 
        raise Exception(f"Error running main funtion: {e}")

if __name__ == '__main__':
    main() 


