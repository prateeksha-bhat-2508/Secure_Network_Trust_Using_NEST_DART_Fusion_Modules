class Fitness:

    def __init__(self, df):
        self.df = df

    def compute(self):

        self.df["Fitness"] = (

            0.5*self.df["BARM_Score"]

            +0.3*self.df["Routing_Score"]

            +0.2*(1-self.df["Attack_Probability"])

        ).clip(0,1)

        return self.df