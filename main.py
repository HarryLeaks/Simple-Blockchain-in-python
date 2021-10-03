from Blockchain import Blockchain
from Block import Block

#initialize blockchain
blockchain = Blockchain()

#mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

#print out each block in the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next