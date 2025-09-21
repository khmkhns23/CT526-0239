# main.py
from mylib import myfunct

period = int(input("How many turns you want to run "))
print("-" * 50)

for i in range(1, period+1):
    print(myfunct("Hi!", i))  