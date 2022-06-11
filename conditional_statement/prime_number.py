num=2
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
        print("prime")
print("---------------------------------------------------------------------")
a = 2
b = 100

"""print("Prime numbers between", lower, "and", upper, "are:")"""

for num in range(a, b+ 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
            print(num)