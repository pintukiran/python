#for loop & while loop
import array as arr
a=arr.array('i',[1,2,3,4,5,67,8])
b=0
print("Array values")
for x in a:
    print(x)
print("----------------------------------")
for x in a[0:5]:
    print(x)
while b<len(a):
    print(a[b])
    b=b+1