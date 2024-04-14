# main file

# import datetime module to get the current time
from datetime import datetime

# import Block class
from BlockClass import Block

# import Blockchain class
from BlockchainClass import BlockChain


# main method
def main():

    # create a blockchain
    captain_coin = BlockChain()

    # print the captain_coin is being created
    print("Captain coin mining in progress...\n")

    # create a new block with index as 1, current_timestamp as current time and data
    new_block_1 = Block(1, datetime.now(), {
                    "sender": "Tony",
                    "receiver": "Henry",
                    "quantity": 50
                })

    # add the new_block on the blockchain
    captain_coin.add_new_block(new_block_1)

    # create one more new block with index as 2, current_timestamp as current time and data
    new_block_2 = Block(2, datetime.now(), {
                    "sender": "Steve",
                    "receiver": "Nick Fury",
                    "quantity": 30
                })

    # add the new_block on the blockchain
    captain_coin.add_new_block(new_block_2)

    # check the validity of the blockchain
    valid = captain_coin.check_blockchain_validity()

    # if the chain is valid, print the chain is valid otherwise invalid
    if (valid):
        print("captain coin blockchain is valid!\n")

        # prin the captain_coin chain
        for block in captain_coin.blockchain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.current_timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Counter: {block.counter}")
            print()

    else:
        print("captain coin chain is invalid!")

# call the main
main()
