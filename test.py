
import time 
from time import sleep
for i in range(0,20):
    start = time.time()
    print("Hello")
    sleep(1)
    end = time.time()
    duration = end - start 
    print(duration)