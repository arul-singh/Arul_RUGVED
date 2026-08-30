#Write a program to print the Fibonacci Sequence till n-values where n is user input.

from functools import cache

n = int(input("Enter the number: ").strip())

@cache
def fibonacci(num):
    
    if num ==0:
        return 0
    if num ==1:
        return 1
    
    return fibonacci(num-1) + fibonacci(num-2)

seq = []

for i in range(int(n)+1):
    seq.append(fibonacci(i))

print(seq)