import hashlib
import sys 
import random

transaction = ""
nonce = 0 
# Proof of Work (PoW) is the consensus mechanism used by blockchains like Bitcoin to validate transactions and secure the network.
# A blockchain consists of many blocks which are interlinked with each other. These blocks contain the transactions and a nonce (number used once)
# Eventually a new block will have to get added to this chain. To do that, transactions are grouped inside of block. 
# Then they get hashed. Theyre hash has to start with a certain number of zeros, in order to be validated. 
# Therefore not only the transaction but also a nonce gets hashed, if the block hash does not start with the required amounts of zeros it will get adjusted.
# Because the output of a hasing algorithm is not predicable. This takes a lot of work by computers. But only so, blockchain networks can ensure the safety of their data. 
# The person who finds the nonce will get a certain amount of crypto currency, depending on the block reward. 
# This programm should demonstrate how that works, in case you are new to the topic of crypto. 
for i in range(0,1): # the loop will iterate one time 
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    sender = random.choice(letters) # random transaction gets created, therefore a random letter gets picked for the sender
    receiver = random.choice(letters)  # the same happens for the receiver of the tranaction, only letters are used 
    amount = random.choice(numbers) # the amount of money is also created randomly 
    transaction_str = f"{sender} has sent {receiver} {amount} {nonce}"  # nonce in the beginning zero 
    print(f"Generated transaction: {transaction_str}")          

            

for i in range(0,1000000000000):  # number may needs to be adjusted depending on the block diff of the network 
    nonce = i 
    transaction_str = f"{sender} has sent {receiver} {amount} {nonce}"
    transaction_hash = hashlib.sha256(transaction_str.encode("utf-8")).hexdigest() # gets hashed
    if transaction_hash.startswith("00000"): # with that you set the block diff of the network (how difficult is it to find the nonce) 
        print("Valid Nonce found: " + str(i))
        print(transaction_hash)
        sys.exit()
    else:
        print("current hash: " + transaction_hash )
        transaction_str = f"{sender} has sent {receiver} {amount} "
        print(i)
    
