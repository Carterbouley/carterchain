from carter_chain.crypto import hash_this
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        contents = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hash_this(contents)

    def __repr__(self):
        return 'index {} hash {}'.format(self.index, self.hash)
        