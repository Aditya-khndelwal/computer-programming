#Q17 = Define a recursive function fibonacci that returns the nth Fibonacci number.

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a,end=",")
        print(b,end=",")
        for i in range(n-2):
            c = a+b
            print(c,end=",")
            a,b=b,c
number = int(input("enter the number of terms you want:"))
fibonacci(number)
