'''
Break statement:-

The break statement is used to terminate the loop or statement in which it is present.
 After that, the control will pass to the statements that are present after the break statement, if available.
If the break statement is present in the nested loop, then it terminates only those loops which contains break statement.
'''
from time import clock_settime


av=5
x=int(input("How many candies you want"))
i=1
while i<=x:
    if i>av:
        print("out of the stock")
        break
    print("candy" ,i)
    i+=1


# Python program to demonstrate
# break statement
  
# Python program to 
# demonstrate break statement 
    
s = 'kiran'
# Using for loop 
for letter in s: 
    
    print(letter) 
    # break the loop as soon it sees 'e' 
    # or 's' 
    if letter == 'i' or letter == 'a':  
        break
    
print("Out of for loop") 
print() 


print("////////////////////////////////////////////")
#continue statement:-

for i in range(1,21):
    if(i%3!=0):
        continue
    else:
        print(i)

for j in "kiranpintu":
    if j=="p" or j=="i":
        pass
    print(j)