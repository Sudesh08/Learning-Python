# 6. Count Vowels in a String
# Create a function that takes a string and counts the number of vowels in it using a loop and condition.
from itertools import count


def checkVowelOrNot(word):
    c=0
    vowel = "aeiou"
    for char in word.lower():
        if char in vowel:
            c+=1
    return c
        # print("got" if word[i]=="u" else "Not found")




enterValueString=input("Enter any word : ")
print("Total number of vowel in ", enterValueString," is ",checkVowelOrNot(enterValueString))