#python program to check if given number is a hill number 
number_to_check = input("Enter a number: ")

def is_hill_number(number):
    number=str(number)

    if len(number)<3:
        return False

    i=0
    
    while number[i]<number[i+1]:
        i= i+1
    
    while i+1<len(number) and number[i]>number[i+1]:
        i = i+1
    
    if i + 1 == len(number):
        return True

    else:
        return False
    

print(is_hill_number(number_to_check))



















