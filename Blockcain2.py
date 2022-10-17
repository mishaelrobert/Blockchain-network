from Block import SHA256
from Transaction import Transaction
T_MCoins = []
transactions = []
last_transaction_index=0

class Blockchain2:
    last_block_hash = ''

    def dump_blockchain(self):
        print("Number of blocks in the chain: " + str(len(self)))
        for x in range(len(T_MCoins)):
            block_temp = T_MCoins[x]
            print("block # " + str(x))
            for transaction in block_temp.verified_transactions:
                Transaction.display_transaction(transaction)
                print('--------------')
            print('=====================================')


    def preformActiveTransactions(self):

        rewardTx = Transaction(
            "Reward",
            self.identity,
            10.0
        )
        self.verified_transactions.push(rewardTx)

        # self.pendingTransactions = [Transaction(null, miningRewardAddress, this.miningReward)];
        # self.rewardSum+=self.miningReward;
        # self.pendingTransactions = [4]
