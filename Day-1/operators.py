#OPERATORS IN PYTHON
#1. ARITHMETIC OPERATOR
a=34
b=24
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a//b=',a//b)
print('a**b=',a**b)

#2. COMPARISON OPERATOR
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#3. LOGICAL OPERATOR
c=True
d=False
print(c and c)
print(c and d)
print(c or c)
print(c or d)

print(not(True))
print(not(False))

#4. ASSIGNMENT OPERATOR
a=98
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a**=2
print(a)
a%=2
print(a)
a//=2
print(a)

#5. MEMBERSHIP OPERATORS
names=["riya","radhu","radhika"]
print("radhu" in names)
print("radhu" not in names)
print("meena" not in names)
print("meena" in names)

#6. IDENTITY OPERATORS
print(a is b)
print(a is not b)