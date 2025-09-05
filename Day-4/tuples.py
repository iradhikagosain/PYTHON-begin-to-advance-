names=('riya','radhika','mahi','mayank','richa','sonia')
print(type(names))
#names[2]='cutie'#tuples are not changeable
print(names[2])

Age=(8)
print(type(Age))
age=(4, )
print(type(age))
mixed=('hello',34,2.5,5+5j)
print(mixed)

#tuple methods
cgpa=(2,5,7,2,5,33,56,3,67,3,2,34,46,5)
print(cgpa.count(2))
print(cgpa.index(67))

#tuple unpacking
tup=(3,6,3)
a,b,c=tup
print(a,b,c)