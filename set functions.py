#printing set
set = {1.0, "Hello", (1, 2, 3)}
print(set)
print('\a')
#printing type
print(type(set))
#addig an element
print('\a')
set.add('name')
print(set)
#updateing set
print('\a')
set.update(['helloworld'])
print(set)
#discard an element
print('\a')
set.discard("Hello")
print(set)
# remove an element
print('\a')
#poping an element
print(set.pop())
print('\a')
print(set)
#clearing set
set.clear()
print(set)
set0={1,2,3,4}
set1={3,4,5,6}
#union of set
print('\a')
print('The union :',set0 | set1)
#OR YOU CAN USE union()
print('\a')
print('The union in another method:',set0.union(set1))
#intersection
print('\a')
print('The intersection :',set0&set1)
#OR YOU CAN USE intersection()
print('\a')
print('The intersection in another method :',set0.intersection(set1))
#difference of two sets
print('\a')
print('The difference:',set0.difference(set1))
#OR YOU CAN USE '-'
print('\a')
print('The difference in another method:',set0-set1)
#symertical difference
print('\a')
print('The symetrical difference',set0^set1)
#OR we can use symetrical_difference()
print('\a')
print('The symetrical difference in another method:',set0.symmetric_difference(set1)) 

