import hashlib


class Encryption:

    def __init__(self,df):
        self.df=df

    def compute(self):

        self.df["Encrypted_ID"]=self.df["Node_ID"].apply(

            lambda x: hashlib.sha256(

                str(x).encode()

            ).hexdigest()

        )

        return self.df