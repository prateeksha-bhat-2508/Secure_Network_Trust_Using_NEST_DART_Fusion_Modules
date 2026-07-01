import hashlib
import json


class Verification:

    def __init__(self, blockchain):

        self.chain = blockchain

    def verify(self):

        for i in range(1, len(self.chain)):

            prev = self.chain[i-1]["hash"]

            if self.chain[i]["prev_hash"] != prev:

                return False

        return True