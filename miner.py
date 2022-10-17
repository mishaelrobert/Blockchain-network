from Block2 import Block2
from Blockcain2 import *
from Client import Client


Tom = Client()
Mishael = Client()

tx0 = Transaction(
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
    Mishael,
    Tom.identity,
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

transactions.append(tx0)
transactions.append(tx1)
transactions.append(tx2)
transactions.append(tx3)
transactions.append(tx4)



def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '0' * difficulty
    for i in range(100000):
        digest = SHA256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print("after " + str(i) + " iterations found nonce: " + digest)
            block.previous_block_hash = (Blockchain2).last_block_hash
            digest = hash(block)
            T_MCoins.append(block)
            (Blockchain2).last_block_hash = digest
            T_MCoins.preformActiveTransactions()
            return digest

    return "could not find a block"



#main node(miner)
block1 = Block2()

#the two other nodes
block2 = Block2()
block3 = Block2()

for i in range(3):
   temp_transaction = transactions[i]
   block1.verified_transactions.append(temp_transaction)
   last_transaction_index += 1
block1.Nonce = mine(block1,1)
#reward will be added at the mine method




Blockchain2.dump_blockchain(T_MCoins)

