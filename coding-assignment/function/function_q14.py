#Q14 = Write a function filter_even that takes a list and returns a list of only the even numbers.

def filter_even(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            continue
    print("filtered list is:",even)
numbers = list(map(int,input().split()))
filter_even(numbers)
