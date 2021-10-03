from Block import Block

#defining a blockchain data structure
class Blockchain:
    diff = 20 #mining difficulty
    maxNonce = 2**32 #we can store in a 32-bit number
    target = 2 ** (256-diff) #target hash for mining

    block = Block("Genesis") #generates the first block in the blockchain
    head = block #sets it as the head of our blockchain

    #adds the block to the chain of blocks
    def add(self, block):
        block.previous_hash = self.block.hash() #Set the hash of a given block as our new block's previous hash
        block.blockNo = self.block.blockNo + 1 #set the block of our new block with adding 1 since its next in the chain

        self.block.next = block #set the next block of the genesis block the block we added
        self.block = self.block.next #set the next block as our current block

    #determines whether or not we can add a given block to the blockchain
    def mine(self, block):
        #from 0 to 2^32
        for n in range(self.maxNonce):
            #is the value of the given block's hash less then out traget value?
            if int(block.hash(), 16) <= self.target:
                #if so, add the block to the chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


