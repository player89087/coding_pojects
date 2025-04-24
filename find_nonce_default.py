import hashlib
import sys 
import time
import os
data_hash = ""
x = 1
start = time.time()
start += 5
for i in range(0,1000000000):
    
    data = i
    data_hash = str(data_hash)
    data = str(data)
    data_hash = hashlib.sha256(data.encode("utf-8")).hexdigest()
    print(f"Hash: {data_hash}")  
    if data_hash.startswith("0"*x) :
        end = time.time()
        os.system('cls||clear')
        print(f"The Hash with {x}  zeros was found." )
        print(data_hash)
        print(f"The Nonce is  {i}")
        x += 1
        duration = end - start 
        duration -= 5
        start = time.time()
        print(f"The needed time was {duration}")
        i = str(i)
        duration = str(duration)
        with open("nonce_time.txt","a") as file:
            file.write("The hash is " + data_hash + "\n" + "The nonce is "+ i + "\n" + "The time is " + duration + "\n" + i + "\n" + "\n")
        i = int(i)
        duration = float(duration)
        time.sleep(5)
        
         

    data = int(data)
    i += 1


 