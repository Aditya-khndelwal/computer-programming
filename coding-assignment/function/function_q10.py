#Q10 = Create a function count_vowels that takes a string and returns the number of vowels in it.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count += 1
        else:
            continue
    print("The number of vowels in given string is:",count)
s = input("enter the string:")
count_vowels(s)
