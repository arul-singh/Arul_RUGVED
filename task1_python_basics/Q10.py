from math import *

def isValid(num):
    
    num = list(str(num))
    num.reverse()
    
    def specific_doubler(sd):
        sd = list(str(sd))
        return (int(sd[0])+int(sd[1]))
    
    i= 1
    for i in range(1, len(num), 2):
        if int(2*(int(num[i])))<9:
            num[i]=int(2*int((num[i])))
        else:
            num[i] = specific_doubler(int(2*int((num[i]))))
    
    num = [int(x) for x in num]
    
    sum_val = sum(num[:])
    
    if sum_val%10==0:
        return True
    else:
        return False
 

    



        