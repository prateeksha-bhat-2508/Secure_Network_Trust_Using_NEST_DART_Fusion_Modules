class Consensus:

    def __init__(self, blockchain):
        self.chain = blockchain

    def compute(self):

        trust = [b["trust"] for b in self.chain]

        return sum(trust)/len(trust)