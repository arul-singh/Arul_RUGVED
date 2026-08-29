#14. Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

arr = str(input("Enter the array with elements separated by space: "))
arr = list("".join(arr.split()))


arr = [str(x) for x in arr]

arr_set = list(set(arr))

couple = {}

for i in arr_set:
    
    if arr.count(i)>1:
        couple[arr.index(i)] = i


lower = min(couple.keys())
print(f"first repeating element is '{couple.get(lower)}' and its index is '{lower}'")
    