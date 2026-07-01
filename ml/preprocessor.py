import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:

    def __init__(self):

        self.encoders = {}

    def fit_transform(self, df):

        df = df.copy()

        # Drop columns not useful for training
        drop_cols = ["id", "attack_cat"]

        for col in drop_cols:
            if col in df.columns:
                df.drop(columns=col, inplace=True)

        y = df.pop("label")

        # Encode categorical columns
        for col in df.select_dtypes(include="object").columns:

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(df[col].astype(str))

            self.encoders[col] = encoder

        return df, y

    def transform(self, df):

        df = df.copy()

        drop_cols = ["id", "attack_cat"]

        for col in drop_cols:
            if col in df.columns:
                df.drop(columns=col, inplace=True)

        y = df.pop("label")

        for col in df.select_dtypes(include="object").columns:

            if col in self.encoders:

                df[col] = self.encoders[col].transform(
                    df[col].astype(str)
                )

        return df, y