class QueueManager:

    def __init__(self, df):
        self.df = df

    def compute(self):

        self.df["Queue_Priority"] = (

            self.df["Attack_Probability"]

            + (1-self.df["Routing_Score"])

        )

        self.df["Queue_Priority"] = self.df["Queue_Priority"].rank(

            ascending=False,

            method="dense"

        )

        return self.df