#To check wether the number is prime numbr or or not
#using in for loop
n = int(input("Enter a number: "))
count=0
for i in range(2,n):
    if n%i == 0:
        count=count+1
if count>1:
    print('It is not a prime number')
else:
    print('It is prime number') 

