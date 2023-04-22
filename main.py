import datetime
import hashlib
import json


class Block:

    def __init__(self, block_index, timestamp, block_data,transaction):
        self.block_index = block_index
        self.timestamp = timestamp
        self.previous_hash = "0"
        self.transaction = transaction
        self.block_data = block_data
        # self.block_data = "-".join(transaction) + "-" + self.previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "Block Index": self.block_index,
            "timestamp": str(self.timestamp),
            # "Creator ID": self.creator_ID,
            # "Owner ID": self.owner_ID,
            "transaction": self.transaction,
            "previous_hash": self.previous_hash,
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()


class Chain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "0", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_transaction(self, sender, recipient, amount):
        # add a new transaction to the list of transactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Create a new blockchain
potter_coin = Chain()

# Add some blocks to the blockchain
potter_coin.add_block(Block(1, str(datetime.datetime.now()), 123 , 234))
potter_coin.add_block(Block(2, str(datetime.datetime.now()), 123, 346))

# Print the blockchain
print(json.dumps([block.__dict__ for block in potter_coin.chain], indent=4))

# Check if the blockchain is valid
print(f"Is blockchain valid? {potter_coin.is_chain_valid()}")
