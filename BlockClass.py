# import the hashlib module to compute hash for the blocks
import hashlib

# import json module to convert json objects to string format
import json

# define a block class to create the blocks
class Block:
    
    # constructor to initialize the block
    # with index, current_timestamp, data, previous_hash as inputs
    def __init__(self, index, current_timestamp, data, previous_hash = " "):

        # assign the index
        self.index = index

        # assign the current_timestamp
        self.current_timestamp = current_timestamp

        # assign the data
        self.data = data

        # assign the previus_hash value
        self.previous_hash = previous_hash

        # initialize the counter to 0
        self.counter = 0

        # compute the hash
        self.hash = self.compute_hash()


    # define a method to compute the hash for the block
    def compute_hash(self):
        # convert the index to string
        index_string = str(self.index)

        # convert the previous_hash to string
        previous_hash_string = str(self.previous_hash)

        # convert the current_timestamp to string
        current_timestamp_string = str(self.current_timestamp)

        # convert the JSON data object to JSON string
        data_string = json.dumps(self.data)

        # convert the counter to string
        counter_string = str(self.counter)

        # concatenate the strings
        concatenated_string = (index_string + previous_hash_string +
            current_timestamp_string + data_string + counter_string)

        # encode the concatenated_string
        encoded_string = concatenated_string.encode() 

        # calculate the hash
        hash_value = hashlib.sha256(encoded_string)

        # get the hexa decimal representation of the hash_value
        hash_value_in_hex = hash_value.hexdigest()

        # return the hash_value_in_hex
        return hash_value_in_hex

    # define a method to employ the proof of work to increase
    # the difficulty in mining or adding new blocks in the chain
    def proof_of_work(self, difficulty):

        # check if self.hash has 'difficulty' number of zeroes in the beginning
        while (self.hash[0:difficulty] != '0' * difficulty):

            # increment the counter
            self.counter += 1

            # compute the hash
            self.hash = self.compute_hash()

            

    # str method to inspect the block
    def __str__(self):
        return(
            f"Index: {self.index}\n"
            f"Timestamp: {self.current_timestamp}\n"
            f"Data: {self.data}\n"
            f"Previous hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
            f"Counter: {self.counter}\n"
        )
        
            

        
