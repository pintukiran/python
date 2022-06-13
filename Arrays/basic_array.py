#first method
import array
a=array.array('i',(1,2,3,4,5,6))
print(a)

#second method
import array as arr
b=arr.array('f',[1,2.7,3,4,5,6,7])
print(a)

#Third method
from array import*
c=array('d',[1,2,3,4,5,6,7,8,9])
print(a)

#Accessing Array elements

print(b[1])
print(a[-2])
print(c[-1])