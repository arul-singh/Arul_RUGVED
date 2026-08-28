word1 = str(input("Enter first word: "))
word2 = str(input("Enter second word: "))

def isAnagram(w1, w2):
    
    if sorted(w1.lower()) == sorted(w2.lower()):
        return True
    else:
        return False

if isAnagram:
    print("The words are anagram")
else:
    print("The words are not anagram")
    
