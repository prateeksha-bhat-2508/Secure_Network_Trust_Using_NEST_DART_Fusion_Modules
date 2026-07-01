import hashlib
import json


class Ledger:

    def __init__(self, df):

        self.df = df

    def generate(self):

        blockchain = []

        previous_hash = "0"

        for _, row in self.df.iterrows():

            block = {

                "node": row["Node_ID"],

                "trust": float(row["Trust_Value"]),

                "barm": float(row["BARM_Score"]),

                "adrs": float(row["ADRS_MPIQ_Score"]),

                "prev_hash": previous_hash

            }

            current_hash = hashlib.sha256(

                json.dumps(block).encode()

            ).hexdigest()

            block["hash"] = current_hash

            blockchain.append(block)

            previous_hash = current_hash

        return blockchain