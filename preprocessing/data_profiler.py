import pandas as pd


class DataProfiler:

    def __init__(self, df):
        self.df = df

    def profile(self):

        print("\n" + "="*70)
        print("DATASET PROFILE")
        print("="*70)

        print("\nShape:")
        print(self.df.shape)

        print("\nColumns:")
        print(self.df.columns.tolist())

        print("\nData Types:")
        print(self.df.dtypes)

        print("\nMissing Values:")
        print(self.df.isnull().sum())

        print("\nUnique Values:")
        print(self.df.nunique())

        print("\nStatistical Summary:")
        print(self.df.describe(include="all"))

        if "label" in self.df.columns:
            print("\nLabel Distribution:")
            print(self.df["label"].value_counts())

        if "type" in self.df.columns:
            print("\nAttack Types:")
            print(self.df["type"].value_counts())

        if "proto" in self.df.columns:
            print("\nProtocols:")
            print(self.df["proto"].value_counts())

        if "service" in self.df.columns:
            print("\nServices:")
            print(self.df["service"].value_counts())

        if "conn_state" in self.df.columns:
            print("\nConnection States:")
            print(self.df["conn_state"].value_counts())