
from time import time
from blockchain import Blockchain
from transaction import Transaction

crypto = Blockchain()

print("(A) Started to mine...")

crypto.createTrans(Transaction("(B)", "(C)", 0.01))
crypto.createTrans(Transaction("(D)", "(E)", 100))
crypto.createTrans(Transaction("(E)", "(F)", 0.2))

initDate = time()
crypto.minePendingTrans("(A)")
endDate = time()

print(f"(A) it took {endDate - initDate} secs")

print('-' * 20)
print(f"(A) has {str(crypto.getBalance('(A)'))} coins in his wallet")
print('-' * 20)

for x in range(len(crypto.chain)):
    print(f"Block hash {x}: {crypto.chain[x].hash}")