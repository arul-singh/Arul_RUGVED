#5. Find the fibonacci of a given number using recursion.

#i optimisde it using @cache 
from functools import cache

try: 
    num = int(input("Enter an Integer: "))
    @cache
    def fibonacci(num):
    
        if num ==0:
            return 0
        if num ==1:
            return 1
    
        return fibonacci(num-1) + fibonacci(num-2)
        
    print(fibonacci(num))
except:
    print("invalid input")


