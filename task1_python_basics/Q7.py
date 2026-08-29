#Write a program to print the Fibonacci Sequence till n-values where n is user input.

text = input(str("Enter a text: "))
shift = int(input("Enter the shift: "))


def Encrypt(text):
    text = list(text)
    
    for i in range(len(text)):
        text[i]= chr(ord(text[i])+shift)
        if text[i]==" ":
            continue
        i += 1
        
    encrypted_text = [x if x != "#" else " " for x in text]
    
    encrypted_text = "".join(encrypted_text)
    
    return "".join(encrypted_text)


print(Encrypt(text))

