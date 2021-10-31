import hashlib

class Block:

    def __init__(self, timeStamp, tx, prevBlock = '') -> None:
        self.timeStamp = timeStamp
        self.tx = tx
        self.prevBlock = prevBlock
        self.difficultyIncrement = 0
        self.hash = self.calculateHash(tx, timeStamp, self.difficultyIncrement)

    def calculateHash(self, data, timeStamp, difficultyIncrement):
        data = str(data) + str(timeStamp) + str(difficultyIncrement)
        data = data.encode()
        hash = hashlib.sha256(data)
        return hash.hexdigest()

    def mineBlock(self, difficulty):
        difficultyCheck = "0" * difficulty

        while self.hash[:difficulty] != difficultyCheck:
            self.hash = self.calculateHash(self.tx, self.timeStamp, self.difficultyIncrement)
            self.difficultyIncrement += 1
