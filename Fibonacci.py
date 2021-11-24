

terms=int(input("Enter the number of terms you want in Fibonacci series :"))
n1,n2=0,1
count=0
if(terms<=0):
    print("Enter a positive integer")
elif(terms==1):
    print("The first number of Fibonacci series is",n1)
else:
    print("The first",terms,"are")
    while(count<=terms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1