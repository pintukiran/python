print("---Using a temporary variable----")
a=11
b=7
temp=a
a=b
b=temp
print(a)
print(b)
print("------Without a temporary variable (Tuple swap)-----------")
a=11
b=7
a,b=b,a
print(a)
print(b)
print("--------Using arithmetic operators (for numbers only)-----")
a=11
b=7
a=a+b
b=a-b
a=a-b
print(a)
print(b)