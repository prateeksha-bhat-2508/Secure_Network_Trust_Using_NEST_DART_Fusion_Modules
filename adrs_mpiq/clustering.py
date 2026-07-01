class Clustering:

    def __init__(self, df):
        self.df=df

    def compute(self):

        self.df["Cluster"]=(

            self.df["Fitness"]>self.df["Fitness"].median()

        ).astype(int)

        return self.df