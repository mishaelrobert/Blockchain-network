from hashlib import sha256

from Block2 import Block2
from Blockcain2 import *
from Client import Client
from Transaction import Transaction
from Block import Block
from BlockChain import BlockChain
from merkle_tree import MerkleTree, hash_data

if __name__=='__main__':

#init blockchain
    blockchain=BlockChain()

    Tom = Client()
    Mishael = Client()


    tx0 = Transaction (
        "Genesis",
        Tom.identity,
        500.0
    )
    tx1 = Transaction(
    Tom,
    Mishael.identity,
    5.0
    )

    tx2 = Transaction(
    Tom,
    Mishael.identity,
    5.0
    )

    tx3 = Transaction(
    Tom,
    Mishael.identity,
    5.0
    )
    tx4 = Transaction(
    Tom,
    Mishael.identity,
    5.0
    )
    tx1.sign_transaction()
    tx2.sign_transaction()
    tx3.sign_transaction()
    tx4.sign_transaction()

    transactions.append(tx1)
    transactions.append(tx2)
    transactions.append(tx3)
    transactions.append(tx4)

    #if you wish to show transaction run the following code
    # for transaction in transactions:
    #     Transaction.display_transaction(transaction)
    #     print ('--------------')

    #
    # #creating first block
    # block0 = Block2()
    # block0.previous_block_hash = None
    # Nonce = None
    # block0.verified_transactions.append (tx0)
    # digest = hash (block0)
    # last_block_hash = digest
    # T_MCoins.append (block0)
    # Blockchain2.dump_blockchain(T_MCoins)
    #
    #
    #




    difficulty=4 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("start mining to make our transactions happen")
    block=Block(transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7')
    block.newHash=block.mineBlock(4)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print("the block hush that was found:",block.newHash)


