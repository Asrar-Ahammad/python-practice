name= input('Enter your name :')
age=int(input('Enter your address:'))
currentbillcode=input('Enter your serial number :')
bill=int(input('Enter amount:'))
l=[name,age,currentbillcode,bill]#creating a list
print('NAME :',l[0])
print('Address:',l[1])
print('Serial number :',l[2])
print('YOUR BILL FOR ELECTRICITY IS ','Rs.',l[3])

