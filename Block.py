import datetime
import hashlib

#block data structure
class Block:
    blockNo = 0 #first block
    data = None #data stores in this block
    next = None #pointer to the next block
    hash = None #hash of this block
    nonce = 0 #number only used once
    previous_hash = 0x0 #store the hash of the previous block in the chain
    timestamp = datetime.datetime.now() #timestamp

    #constructor of the block and stores some data
    def __init__(self, data):
        self.data = data

    #function to compute 'hash' of a block
    def hash(self):
        h = hashlib.sha256() #generates an 256bit signature that represents some piece of text
        #the input of the sha256 algorithm will be a concatenated string consisting of 5 block attributes
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest() #returns a hexadecimal string

    def __str__(self):
        #print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str (self.nonce) + "\n-----------"
              