# import the Block class 
from BlockClass import Block

# define the BlockChain class to chain the blocks together
class BlockChain:
    
    # constructor to initialize the blockchain
    def __init__(self):

        # assign the blockchain by calling create_initial_block
        self.blockchain = [self.create_initial_block()]

        # set the difficulty to 4
        self.difficulty = 4

        

    # define a method to create the initial block
    def create_initial_block(self):
        
        # create a initial block
        # with index as 0, timestamp as 01/01/2020
        # data as hardcoded value and previous_hash as 0
        initial_block = Block(0, "01/01/2020", "Initial block", 0)

        # return the initial_block
        return initial_block


    # define a method to get the latest block from the blockchain
    def get_latest_block(self):

        # latest block is always added at the end
        # therefore the return the last block from the blockchain array
        return self.blockchain[-1]

    # define a method to add a new block to the blockchain
    def add_new_block(self, new_block):

        # set the previous block hash value as previous_hash on the new_block
        new_block.previous_hash = self.get_latest_block().hash

        # compute the hash for the new block
        # new_block.hash = new_block.compute_hash()

        new_block.proof_of_work(self.difficulty)

        # add the new block on the blockchain array
        self.blockchain.append(new_block)

    # define a method to check the blockchain validity
    def check_blockchain_validity(self):

        # iterate through each block and check the validity of chain
        for index in range(1, len(self.blockchain)):

            # check  whether each block has previous block's hash value
            # as its previous_hash value
            current_block = self.blockchain[index]
            previous_block = self.blockchain[index - 1]

            if (current_block.previous_hash != previous_block.hash):

                # if not return false
                return False

            # check whether the hash on current block is equal to the computed hash value
            if (current_block.hash != current_block.compute_hash()):
            
                # if not return false
                return False

            # return true if all the checks are passed
            return True
            
        
