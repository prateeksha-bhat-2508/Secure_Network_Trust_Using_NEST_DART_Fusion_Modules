class TrustManager:

    def __init__(self, df):
        self.df = df

    def compute(self):

        self.df["Trust_Value"] = (

            0.40*self.df["BARM_Score"]

    +0.40*self.df["ADRS_MPIQ_Score"]

    +0.20*self.df["Unified_Trust_Evidence"]


        ).clip(0,1)

        return self.df