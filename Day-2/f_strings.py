#F STRINGS
name='radhika gosain'
age=20
address='jalandhar'
cgpa=8.5
print(f'my name is {name} ,my age is {age} i live in {address} and i got {cgpa} cgpa this year')#f string
print("my name is {} and age is {}".format(name,age))#format string

x=78
y=28
print("x is {} and y is {} so tal is {}".format(x,y,x+y))

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.3f}")

text = "riya"
print(f"{text:>9}")  # Right align
print(f"{text:<9}")  # Left align
print(f"{text:^9}")  # Center align