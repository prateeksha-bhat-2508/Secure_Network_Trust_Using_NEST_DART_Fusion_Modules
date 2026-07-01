import pandas as pd
from utils.logger import logger


class DataCleaner:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_duplicates(self):
        before = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after = len(self.df)

        logger.info(f"Removed {before-after} duplicate rows.")

        return self

    def handle_missing(self):

        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        categorical_cols = self.df.select_dtypes(exclude=["number"]).columns

        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(self.df[col].median())

        for col in categorical_cols:
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        logger.info("Missing values handled.")

        return self

    def remove_constant_columns(self):

        constant_cols = [
            col for col in self.df.columns
            if self.df[col].nunique() <= 1
        ]

        self.df.drop(columns=constant_cols, inplace=True)

        logger.info(f"Removed {len(constant_cols)} constant columns.")

        return self

    def clean(self):

        return (
            self.remove_duplicates()
                .handle_missing()
                .remove_constant_columns()
                .df
        )