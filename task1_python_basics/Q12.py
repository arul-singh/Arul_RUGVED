n=5
for i in range(n+1):
    print(((n-i)*" ")+ (i*"* "))

for i in range(n,0,-1):
    print(((n-i)*" ")+ (i*"* "))
    


n = n+1
for i in range(n):
    print((i*"*") + (((2*n)-1-(2*i))*" ")+ (i*"*"))
    
for i in range(n-2, 0, -1):
    print((i*"*") + (((2*n)-1-(2*i))*" ")+ (i*"*"))
    




