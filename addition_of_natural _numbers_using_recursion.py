def sum(x):
    int(x)
    if x==0:
        return 1
    else:
        return (x + sum(x-1))
num=int(input('Enter a number :'))
print('The sum of natural numbers upto ',num,'is',sum(num))