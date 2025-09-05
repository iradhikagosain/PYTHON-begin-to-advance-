

def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

def addition(a, b, c):
    total = a + b + c
    return total

def greet(name="guest"):
    return f'hello,{name}'

def student(name,age):
    print(f"name:{name},age:{age}")


#Lambda functions
square=lambda x:x*x
area=lambda x,y,z:x*y*z

# Call and print results
print("Sum of numbers:", addition(3,5 ,5))#positional arguements
print("Average of numbers:", average(4,6,2))
print(greet())#default argument
student(age=23,name="radhika")#keyword argument
print(square(6))
print(area(3,5,2))


