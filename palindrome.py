####Write a Python program to check whether a string is a Palindrome or not
##exmple aba=aba

def palin(a):
    if a==a[::-1]:
        return "its a palindrome"
    else:
        return "NOT a palindrome"



a='aba'
print(palin(a))