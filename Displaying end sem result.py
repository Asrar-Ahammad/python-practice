name=input('Enter Student Name :')
course=input('Enter Student Course :')
rrn=input('Enter RRN of Student :')
print('\a')
print('Enter Semester marks')
print('\a')
py1=int(input('Enter Python Theory Marks :'))
py2=int(input('Enter Python Lab Marks:'))
em=int(input('Enter Engineering Mechanics Marks :'))
phy=int(input('Enter Physics Marks :'))
dl=int(input('Enter Digital  Logic Design Marks:'))
mat=int(input('Enter Mathamatics Marks :'))
ai=int(input('Enter Introduction to Artificial Intelligence Marks:'))
evs=int(input('Enter Environmental studies Marks :'))
print('\a')
print('RESULT OF SEMESTER')
print('\a')
print('Student Name :',name)
print('Student Course :',course)
print('Student RRN :',rrn)
if py1<35:
    print('\nMarks secured in  Python Theory',"-",py1)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Python Theory','-',py1)
    print('Result --','Pass')
if py2<35:
    print('\nMarks secured in  Python Lab',"-",py2)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Python Lab','-',py2)
    print('Result --','Pass')
if em<35:
    print('\nMarks secured in  Engineering Mechanics',"-",em)
    print('Result --','Fail')
else:
    print('\nMarks secured in  PEngineering Mechanics','-',em)
    print('Result --','Pass')
if phy<35:
    print('\nMarks secured in  Physics',"-",phy)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Physics','-',phy)
    print('Result --','Pass')
if dl<35:
    print('\nMarks secured in  Digital Logic Design',"-",dl)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Digital Logic Design','-',dl)
    print('Result --','Pass')
if mat<35:
    print('\nMarks secured in  Mathematics',"-",mat)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Mathematics','-',mat)
    print('Result --','Pass')
if ai<35:
    print('\nMarks secured in  Introduction to Artificial Intelligence',"-",ai)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Introduction to Artificial Intelligence','-',ai)
    print('Result --','Pass')
if evs<35:
    print('\nMarks secured in  Environmental studie',"-",evs)
    print('Result --','Fail')
else:
    print('\nMarks secured in  Environmental studie','-',evs)
    print('Result --','Pass')
print('\a')
total=py1+py2+em+phy+dl+mat+ai+evs
maxmarks=800
print('Percentage :',(total/maxmarks)*100)
per=(total/maxmarks)*100
print('\a')
if  per>=95.0:
    print('Grade : S')
elif per>=90.0:
    print('Grade : A')
elif per>=85.0:
    print('Grade : B')
elif per>=80.0:
    print('Grade : C')
elif per>=70.0:
    print('Grade :D ')
elif 35<per<69.9:
    print('Grade :E')
elif per<35.0:
    print('Grade : F')
