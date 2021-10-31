import datetime
import json
import pprint
from block import Block
from transaction import Transaction

class Blockchain:
    
    def __init__(self):
        self.chain = [self.genesisBlock()]
        self.difficulty = 3
        self.pendingTransaction = []
        self.reward = 0.0001

    def genesisBlock(self):
        genesisBlock = Block(str(datetime.datetime.now()), "I'm the zero block")
        return genesisBlock
    
    def getLastBlock(self):
        return self.chain[-1]

    def minePendingTrans(self, minerRewardAddress):
        newBlock = Block(str(datetime.datetime.now()), self.pendingTransaction)
        newBlock.mineBlock(self.difficulty)
        newBlock.prevBlock = self.getLastBlock().hash

        print(f"Previous block hash {newBlock.prevBlock}")

        testChain = []
        for tx in newBlock.tx:
            temp = json.dumps(tx.__dict__, indent=5, separators=(',',':'))
            testChain.append(temp)

        pprint.pprint(testChain)

        self.chain.append(newBlock)

        print(f"Block hash: {newBlock.hash}")
        print("New block added")

        rewardTrans = Transaction("System", minerRewardAddress, self.reward)
        self.pendingTransaction.append(rewardTrans)
        self.pendingTransaction = []

    def isChainValid(self):
        for x in range(1, len(self.chain)):
            currentBlock = self.chain[x]
            prevBlock = self.chain[x - 1]

            if(currentBlock.prevBlock != prevBlock.hash):
                print("The chain is not valid")
            
        print("The chain is valid")

    def createTrans(self, transaction):
        self.pendingTransaction.append(transaction)

    def getBalance(self, walletAddress):
        balance = 0
        for block in self.chain:
            if(block.prevBlock == ""):
                continue
            for transaction in block.tx:
                if(transaction.fromWallet == walletAddress):
                    balance -= transaction.amount
                if(transaction.toWallet == walletAddress):
                    balance += transaction.amount
        return balance
