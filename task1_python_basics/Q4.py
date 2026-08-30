#4. Write a python function to perform selection sort on a given string.

text = str(input("Enter the text: "))

def selection_sort(text: str):
    return "".join(sorted(list("".join(text.lower().split()))))
    
print(selection_sort(text))
