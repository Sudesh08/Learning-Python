#
# 9. Palindrome Checker
# Write a function that checks whether a string is a palindrome (same forwards and backwards)
# using loops and conditions.

def isPalindrome(sen):
    revStr=""
    for i in sen:
        revStr=i+revStr
    if sen==revStr:
        print("Palindrome")
    else:
        print("Not Palindrome")

sentence =input("Enter String to check weather it is palindrome or not")
isPalindrome(sentence)