#Q19 = Write a function palindrome that checks if a given string is a palindrome and print the reversed string as well.
def palindrome(s):
    print("reversed string is:",s[::-1])
    return s == s[::-1] 
s = input("enter string:")
print(palindrome(s))
