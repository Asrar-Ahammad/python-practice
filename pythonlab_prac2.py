class employee:
    def __init__(self,name,age,qua,sal,exp):
        self.name=name
        self.age=age
        self.qua=qua
        self.sal=sal
        self.exp=exp
    def details(self):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Qualification :',self.qua)
        print('Salary :',self.sal)
        print('Experience :',self.exp)
det=employee('Shauib','21','Phd Artificial Intelligence','₹10,00,000/month','1 year')
det.details()
