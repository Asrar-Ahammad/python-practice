serno = int(input("Enter service Number : "))
cname = input("Enter User Name : ")
old = int(input("Enter your old reading : ")) 
new = int(input("Enter your new reading : "))
units = new-old
					
if units <= 100: 
    amount = units*0.90 
    serchg = 25
					
elif units >= 100 and units < 300:
    amount = units*1.50
    serchg = 35
					
elif units >= 300 and units <= 500: 
    amount = units*2.75
    serchg = 45
					
elif units > 500:
    amount = units*4.50 
    serchg = 100
netamount = amount + serchg 
print("Electrical information : ")
print("\tMeter Number : ", serno)
print("\tUser Name : " + cname) 
print("\tOld reading : ", old) 
print("\tNew reading : ", new) 
print("\tTotal units : ", units)
print("\n\tTotal payable amount : Rs.", netamount)

