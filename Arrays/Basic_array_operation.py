#Finding the length of an array
import array as arr
a=arr.array('d',[2.1,3.3,4.5])
print(len(a))

#Adding elements to an array
b=arr.array('i',[2 ,3 ,4,5, 6])
a.append(3.2)
print("Array a=",a)
b.extend([9,8,7])
print(b)
c=arr.array('f',[1,2,6.7,8,9])
c.insert(2,5.6)
print(c)

#Removing elements of an Array

a=arr.array('d',[1.1,2.2,3.8,3.1,3.7])
a.pop()#pop() function remove an element and return it
print(a)
a.pop(1)
print(a)
a.remove(3.8)#remove() function remove an element with a specific value without rreturing it
print(a)

print("----------------------------------------------")
A=arr.array('d',[1.1,2.1,3.1,2.6,7.8])
B=arr.array('d',[9.3,6.4,5.7])
C=arr.array('d')
C=A+B
print("Array C=", C)
#Slicing An Array
print("---Slicing--------------")
n=arr.array('i',[1,2,3,4,5,6])
print(a[0:4])
for x in c[0:6]:
    print(x)
