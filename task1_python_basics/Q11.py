#11. Write a Python program that prints the grade level of a given text using Coleman-Liau formula.

i = 0
input_text = []

print("Enter the text (single line or multiline, press enter twice to end): \n")

while i<1:
    text = str(input(""))
    appendable_text = text.split()
    input_text.append(appendable_text)
    if text == "":
        i+=1

flattened_text = []
for lists in input_text:
    for elements in lists:
        flattened_text.append(elements)

total_letters = sum(1 for char in "".join(flattened_text) if char.isalpha())
total_words =  len(flattened_text)
sentences = sum(1 for char in "".join(flattened_text) if char in ".!?")
flattened_text = " ".join(flattened_text)

L = (total_letters/total_words)*100
S = (sentences/total_words)*100

CLI = (0.0588*L) - (0.296*S) - 15.8

print(round(CLI))

print(flattened_text)
print(total_letters)
print(total_words)
print(sentences)