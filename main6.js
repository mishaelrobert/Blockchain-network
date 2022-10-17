const {
    Blockchain,
    Transaction
} = require('./Blockchain5.js');
const EC = require('elliptic').ec;
const ec = new EC('secp256k1');
//wallet 1 initialization:
const myKey1 =
    ec.keyFromPrivate('50c963fdb1557d9caa85be8e8c8846dc31b1af8fb9d2e9e2cdf13d758a325030')
const myWalletAddress1 = myKey1.getPublic('hex');
//wallet 2 initialization:

const myKey2=
    ec.keyFromPrivate('31ece57e87215b0aca98bf1a10d01f64328dd1e9b0f1d467d5a9931f5f0cc095')
const myWalletAddress2 = myKey2.getPublic('hex');
//we have to build a blockChain every 5-10 seconds
const t_mChain = new Blockchain();

console.log('wallet 1 before transaction:', t_mChain.getBalanceOfAddress(myWalletAddress1));


for(let i=0;i<10;i++)
{
const transaction1 = new Transaction(myWalletAddress1, 'tempAddress2', 0);
const transaction2 = new Transaction(myWalletAddress2, 'tempAddress2', 0);
transaction1.signTransaction(myKey1);
transaction2.signTransaction(myKey2);
t_mChain.addTransaction(transaction1);
t_mChain.addTransaction(transaction2);
t_mChain.minePendingTransaction(myWalletAddress1);
t_mChain.minePendingTransaction(myWalletAddress2);
}




console.log();
console.log('Is blockchain valid?', t_mChain.isChainValid() ? 'yes' : 'no');
JSON.stringify(t_mChain, null, 4);

console.log('Balance for wallet1', t_mChain.getBalanceOfAddress(myWalletAddress1));

console.log('Balance for wallet2', t_mChain.getBalanceOfAddress(myWalletAddress2));


console.log("coins in blockChain:",t_mChain.getBalanceOfAddress(myWalletAddress1)
+t_mChain.getBalanceOfAddress(myWalletAddress2));

console.log("reward for wallets",t_mChain.rewardSum)


const transaction2 = new Transaction(myWalletAddress1, myWalletAddress2, 5);
transaction2.signTransaction(myKey1);
t_mChain.addTransaction(transaction2);
t_mChain.minePendingTransaction(myWalletAddress1);
console.log('Balance for new wallet2', t_mChain.getBalanceOfAddress(myWalletAddress2));


console.log('Balance for old wallet', t_mChain.getBalanceOfAddress(myWalletAddress1));




