class info:
   		 def detail(self):
        			print("My name is ASRAR from AI&DS dept")

class cg(info) :
   		 def cgp(self):
        			print("My CGPA is 9.8")

class adress(cg):
   		 def adre(self):
        			print("I'm from Andhra Pradesh, Chitoor dist.")

obj = adress()
obj.detail()
obj.cgp()
obj.adre()

