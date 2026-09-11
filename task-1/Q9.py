#9. Write a python function to encrypt a string using Ceasar’s Cipher

text = str(input("Enter the text to be encrypted: "))
shift = int(input("Enter the shift: "))

arr = list(text)


for i in range(len(arr)):

    if ord(arr[i]) not in range(65,90) and ord(arr[i]) not in  range(97,123):
        continue
    if ord(arr[i]) + shift in range(65,91):
        if ord(arr[i]) + shift >90:
            arr[i] = chr((90-(ord(arr[i]) + shift)+65))
        else:
            arr[i] = chr(ord(arr[i]) + shift)
    if ord(arr[i]) + shift in range(97,123):
        if ord(arr[i]) + shift >122:
            arr[i] = chr((122-(ord(arr[i]) + shift)+97))
        else:
            arr[i] = chr(ord(arr[i]) + shift)

arr = "".join(arr)
print(arr)


