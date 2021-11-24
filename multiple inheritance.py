class first:  
    		def add(self,a,b):  
        		    return a+b;  
class second:  
    		def mult(self,a,b):  
        		    return a*b;  
class Derived(first,second):  
    		def div(self,a,b):  
        		    return a/b;  
d = Derived()  
print('THE ADDITION :',d.add(4,3))  
print('THE MULTIPLICATION:',d.mult(4,2))  
print('THE DIVISION:',d.div(7,8))

