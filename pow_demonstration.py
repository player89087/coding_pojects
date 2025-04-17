import hashlib
import sys 
import random
import hmac

password_hash = ""
transaction = ""
nonce = 0 

for i in range(0,1):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    global sender 
    sender = random.choice(letters)
    global receiver
    receiver = random.choice(letters)
    global amount 
    amount = random.choice(numbers)
    global transaction_str
    transaction_str = f"{sender} has sent {receiver} {amount} {nonce}"
    print(f"Generated transaction: {transaction_str}")
            

for i in range(0,1000000000000):  
    nonce = i 
    transaction_str = f"{sender} has sent {receiver} {amount} {nonce}"
    transaction_hash = hashlib.sha256(transaction_str.encode("utf-8")).hexdigest()
    if transaction_hash.startswith("00000"):
        print("Valid Nonce found: " + str(i))
        print(transaction_hash)
        sys.exit()
    else:
        print("current hash: " + transaction_hash )
        transaction_str = f"{sender} has sent {receiver} {amount} "
        
        #transaction_hash = hashlib.sha256(transaction.encode("utf-8")).hexdigest()
        print(i)
    

#find_nonce()
    


    # default without additional data  Nonce = 1 = 39, 2 = 286, 3 = 886, 4 = 88484, 5 = 596138 