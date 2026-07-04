import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

class DataPreprocessor:
    """
    A simple preprocessor that:
      - Drops 'id' and 'attack_cat' if present.
      - Encodes object columns with LabelEncoder.
      - Separates features and label ('label' column assumed to be 0/1).
    """
    def __init__(self):
        self.encoders = {}

    def _clean_infinite(self, df):
        return df.replace([np.inf, -np.inf], np.nan)

    def fit_transform(self, df):
        df = df.copy()
        # Drop unnecessary columns if they exist
        drop_cols = ["id", "attack_cat"]
        for col in drop_cols:
            if col in df.columns:
                df.drop(columns=col, inplace=True)

        # Separate label
        if "label" not in df.columns:
            raise ValueError("DataFrame must contain a 'label' column")
        y = df.pop("label").astype(int)

        # Encode categorical columns
        for col in df.select_dtypes(include="object").columns:
            encoder = LabelEncoder()
            # Handle unseen labels by filling with a sentinel (optional)
            df[col] = df[col].astype(str)
            df[col] = encoder.fit_transform(df[col])
            self.encoders[col] = encoder

        # Replace infinities and drop rows with NaN
        df = self._clean_infinite(df)
        df.dropna(inplace=True)

        return df, y

    def transform(self, df):
        df = df.copy()
        drop_cols = ["id", "attack_cat"]
        for col in drop_cols:
            if col in df.columns:
                df.drop(columns=col, inplace=True)

        if "label" not in df.columns:
            raise ValueError("DataFrame must contain a 'label' column")
        y = df.pop("label").astype(int)

        for col in df.select_dtypes(include="object").columns:
            if col in self.encoders:
                df[col] = self.encoders[col].transform(df[col].astype(str))
            else:
                # If a new categorical column appears during transform, treat as unknown
                # Here we simply drop it (or you could raise an error)
                df.drop(columns=col, inplace=True)

        df = self._clean_infinite(df)
        df.dropna(inplace=True)
        return df, y