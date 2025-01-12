import os
import pandas as pd

class OnlineResources():
    pass

class Datasets():
    
    def __init__(self, dataset):
        self.dataset = dataset.lower() #str

        self.available_datasets = {
            'boston': 'boston.csv'
        }

        if self.dataset not in self.available_datasets:
            raise ValueError(
                f"Dataset '{self.dataset}' is not available. "
                f"Choose from {list(self.available_datasets.keys())}."
            )
        
        self.data_assignment()

    def data_assignment(self):
        # This function should look at self.dataset and return a pandas dataframe object of that dataset
        dataset_path = os.path.join(os.path.dirname(__file__), 'datasets', self.available_datasets[self.dataset])
        return pd.read_csv(dataset_path)

