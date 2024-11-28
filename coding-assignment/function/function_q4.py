#Q4 = Define a function is_even that takes a number and returns True if it's even, otherwise False.
def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)
num = int(input("enter the number:"))
is_even(num)
