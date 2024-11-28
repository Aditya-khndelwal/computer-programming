#Q20 = Define a function gcd that calculates the greatest common divisor of two numbers using recursion.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("enter first number:"))
b = int(input("enter second number:"))
print("greatest common divisor is:",gcd(a,b))
