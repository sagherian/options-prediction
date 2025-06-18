class DataLoader:
    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path

    def load_data(self, filename):
        import pandas as pd
        file_path = f"{self.raw_data_path}/{filename}"
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            raise Exception(f"File {filename} not found in {self.raw_data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")

    def get_all_data(self):
        import os
        all_data = []
        for filename in os.listdir(self.raw_data_path):
            if filename.endswith('.csv'):
                data = self.load_data(filename)
                all_data.append(data)
        return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()