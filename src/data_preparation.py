class DataPreparation:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        # Implement data cleaning logic here
        pass

    def transform_data(self):
        # Implement data transformation logic here
        pass

    def split_data(self, test_size=0.2):
        from sklearn.model_selection import train_test_split
        train_data, test_data = train_test_split(self.data, test_size=test_size)
        return train_data, test_data