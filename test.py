from preprocessing.loader import DatasetLoader

loader = DatasetLoader()

df = loader.load_dataset("Network")

print(df.columns.tolist())