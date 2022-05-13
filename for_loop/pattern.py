for i in range(5):
    for j in range(5):
        print("#",end=" ")
    print()

print("//////////////////////////////////////")
for i in range(5):
    for j in range(i+1):
        print("A",end=" ")
    print()


print("//////////////////////////////////////")
for i in range(5):
    for j in range(5-i):
        print("K",end=" ")
    print()

print("//////////////////////////////////////")

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("//////////////////////////////////////")

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
