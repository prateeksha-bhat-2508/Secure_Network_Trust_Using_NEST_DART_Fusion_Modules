class MPIQ:

    def __init__(self,df):
        self.df=df

    def compute(self):

        self.df["ADRS_MPIQ_Score"] = (
    0.3 * self.df["BARM_Score"]
    + 0.3 * self.df["Hybrid_Trust"]
    + 0.2 * self.df["Centrality_Trust"]
    + 0.2 * (1 - self.df["Attack_Probability"])
).clip(0, 1)
        return self.df