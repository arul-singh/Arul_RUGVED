#8. Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence. Example: string=“abcdabcdabcdabcd” n=4 output: “abcd”, “abcd”, “abcd”, “abcd” If the division is not possible or the sequence cannot be same, print out the appropriate error.

string = str(input("Enter the word: "))
n = int(input("Enter the division length: "))

divided_list = []

if len(string)%n != 0:
    print("division is not possible")


for i in string:
    divided_list.append(string[i*n:(i+1)*n])
    i+=1
    

print(divided_list)