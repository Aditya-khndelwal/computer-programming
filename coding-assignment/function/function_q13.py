#Q13 = Define a function all_even that takes a list of numbers and returns True if all numbers are even, otherwise False.
def all_even(numbers):
    if all(num % 2 == 0 for num in numbers):
        print(True)
    else:
        print(False)
numbers = list(map(int,input().split()))
all_even(numbers)
