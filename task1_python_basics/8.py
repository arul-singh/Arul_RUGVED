string = str(input("Enter the word: "))
n = int(input("Enter the division length: "))

divided_list = []

if len(string)%n != 0:
    print("division is not possible")

i = 0

while i <len(string)/n:
    divided_list.append(string[i*n:(i+1)*n])
    i+=1
    

print(divided_list)