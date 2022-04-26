#python list:-
num=[25,26,27,28,29]
print(num)

print("'integer'///////////////////////////////")
print(num[0],num[4])

print(num[-2],num[-4])

print(num[:3])
print(num[2:])
print(type(num))

print("'string'//////////////////////////////////////")
num1=['naveen','kiran','john']
print(num1)
print(num1[-1])

print("///float////////////////////////")
num2=[2.19,29.9,9.20,1.02]
print(num2)

num3=[103,"john",19.20]
print(num3)
#list inside  the list
num5=[num,num1,num2,num3]
print(num5)

print("////////////////////////////////")
#append means add the value or string at last in list
num.append(45)
print(num)
print("///////////////////////////////////////")
#insert add the value or string in b/w 
num.insert(2,77)
print(num)
print("/////////////////")
# if u want to remove the perticular value  use .remove keyword
num.remove(26)
print(num)
print("//////////////////////////////////")
#if u want to remove index ways means use .pop keyword
num.pop(3)
print(num)
print("//////////////////////////////")
#if u want to delete multiple values ,use del keyword
del num[2:]
print(num)
print("//////////////////////////////////////////")
#if u want to add multiple values means use .extend keyword
num.extend([28,34,48,200])
print(num)
print('//////////////////////////////')
#if u want know maximum number use max() keyword
max (num)

'''print("//////////////////////////////")
#if u want know minimum number use min() keyword
min (num)
print(num)
print("////////////////////////")
#if u want sum all the numbers use sum() keyword
sum (num)
print(num)'''

