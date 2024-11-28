
#Q5 = Write a function factorial that calculates the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    else:
        print(n * factorial(n - 1))
n = int(input("enter the number:"))
factorial(n)
