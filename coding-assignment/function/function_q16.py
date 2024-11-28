#Q16 = Write a recursive function sum_digits that sums the digits of a given number.
def sum_digits(n):
    c = 0
    if n == 0:
        return 0
    else:
        while n!=0:
            last_number = n % 10
            n = n // 10
            c += last_number
    print("sum of all digits is:",c) 
n = int(input("enter the number:"))
sum_digits(n)
