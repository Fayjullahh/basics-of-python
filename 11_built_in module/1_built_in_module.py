#some built-in module
#1.math,2.os,3.time,4.random
import math
print(math.sqrt(4))
print(math.pi)
print(math.ceil(3.4))
print(math.floor(3.9))
print(math.factorial(5))
print(math.log2(8))

import random
print(random.randint(1,10))

import time
print(time.localtime())
print(time.ctime()) #CURRENT TIME  
print("Hello")
time.sleep(1)
print("world")

import os
print(os.getcwd()) #get current working directory
print(os.listdir()) #get current working directory