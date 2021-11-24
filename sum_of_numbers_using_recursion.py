#Python program to find the sum of natural numbers up to given number using recursive function
def sum_Num(n):
    if n<= 1:
        return n
    else:
        return n+ sum_Num(n-1)

num=int(input('Enter the number :'))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is :",sum_Num(num))