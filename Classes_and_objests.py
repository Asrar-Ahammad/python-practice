# # Student Details
# class student:
#     def __init__(self,name,dep,rrn,gpa):
#         self.name=name
#         self.dep=dep
#         self.rrn=rrn
#         self.gpa=gpa
#     def details(self):
#         print('Name :',self.name)
#         print('Department :',self.dep)
#         print('RRN :',self.rrn)
#         print('GPA :',self.gpa)
# det=student('Asrar','Artificial Intelligence and Data Science','200171601048','9.4')
# det.details() 

# # Employee details
# class employee:
#     def __init__(self,name,qual,exp,sal):
#         self.name=name
#         self.qual=qual
#         self.exp=exp
#         self.sal=sal
#     def details(self):
#         print('Name :',self.name)
#         print("Qualification :",self.qual)
#         print('Experience :',self.exp)
#         print('Salary :',self.sal)
# det=employee('Shuaib','PHD in Artificial Intelligence','7 years','₹75,00,000 per month')
# det.details()

# # Update and delete
# class marks:
#     def __init__ (self,m,p,c):
#         self.m=m
#         self.p=p
#         self.c=c
#     def display(self):
#         print('MARKS IN MATHS :',self.m)
#         print('MARKS IN PHYSICS :',self.p)
#         print('MARKS IN CHEMISTRY :',self.c)
# de=marks(95,85,90)
# de.display() 
# de.c=95
# de.display()
# del de.c
# de.display() 

# Car program
class Vehical:
    def __init__(self,br,na,col,ty,pr):
        self.br=br
        self.na=na
        self.col=col
        self.ty=ty
        self.pr=pr
    def details(self):
        print('Brand :',self.br)
        print('Name :',self.na)
        print('Color :',self.col)
        print('Type :',self.ty)
        print('Price :',self.pr)
car0=Vehical('FORD','Mustang','Black','Sedan','₹75,00,000')
car0.details()
print('\a')
car1=Vehical('Tata','Harrier','White','SUV','₹15,00,000')
car1.details()
print(car1)

