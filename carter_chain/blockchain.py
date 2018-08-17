import datetime as date
from carter_chain.block import Block

def create_genesis_block():
    date_now = date.datetime.now()
    block = Block(0, date_now, "Genisis Block", "0")
    return block

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

class Blockchain:
    def __init__(self):
        genesis_block = create_genesis_block()
        self.current_chain = [genesis_block]
    
    def __repr__(self):
        return 'chain length {}'.format(len(self.current_chain))

    def add_block(self, new_block):
        print("Adding a block")
        # TODO: verify the block first!
        self.current_chain.append(new_block)

    def last_block(self):
        return self.current_chain[-1]
    
if __name__ == "__main__":
    blockchain = Blockchain()

    print(blockchain)

    for _ in range (0, 20):
        last_block = blockchain.last_block()
        new_block = next_block(last_block)
        blockchain.add_block(new_block)

        print(new_block)

    print(blockchain)
