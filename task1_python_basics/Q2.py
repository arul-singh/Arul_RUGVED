#2. Write a python program to sort a string alphabetically and print the count of each character.


text = "Hello World"

sorted_text = "".join(sorted(list("".join(text.lower().split()))))

print("sorted text: \"" +sorted_text+"\"")

unique_characters = sorted(list(set(sorted(list("".join(text.lower().split()))))))


char_count = {}

for i in range(len(unique_characters)):
    
    char_count[unique_characters[i]]= sorted_text.count(unique_characters[i])
    
print("\nCharacter Counts are- \n")
for a,b in char_count.items():
    print(f"{a} : {b}")
    

