
#Conditional statements
if False:
    print("I'm right person")
else :
    print("I'm not right person")
#if given number is even number or odd number
x=8

if x%2==0:
    print("given number is even")
else :
        print("given number is odd")
#without using else keyword printing given number is even r odd number
x=2
if x%2==0:
    print("number is even")
if x%2==1:
    print("number is odd")
#Nested if :-if inside the if block is called Nasted if
x=2
if x%2==0:
    print("number is even")
    if x<0:
        print("x greater than 2")
    else:
        print("Not greater than 2")
else :
    print("number is odd")
#random numbers checking eg:-2,4,5,6
x=1
if x==2:
    print("one")
elif x==4:
    print("four")
elif x==5:
    print("five")
elif x==6:
    print("six")
else:
    print("wrong statement")
    '''
    if (condition):
            #Set of statement to execute if condition is true
elif (condition):
            #Set of statements to be executed when if condition is false and elif condition is true
else:
       #Set of statement to be executed when both if and elif conditions are false
    '''
    num = 10
if (num < 0):
     print("num is less than zero")
 
elif (num > 15):
       print("num is greater then five")
 
else:
       print("else statement")