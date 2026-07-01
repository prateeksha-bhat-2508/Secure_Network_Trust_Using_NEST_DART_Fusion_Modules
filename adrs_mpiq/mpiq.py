class MPIQ:

    def __init__(self,df):
        self.df=df

    def compute(self):

        self.df["ADRS_MPIQ_Score"]=(

            0.4*self.df["Fitness"]

            +0.3*self.df["Routing_Score"]

            +0.2*self.df["Hybrid_Trust"]

            +0.1*self.df["BARM_Score"]

        ).clip(0,1)

        return self.df