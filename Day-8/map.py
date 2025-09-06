nums=[1,2,4,5,6,35,62,23,5,2]
def square(x):
    return x*x

new=list(map(square,nums))
print(new)


numbers=(34,6,2,5,2)
def area(i):
    return i*i


output=tuple(map(area,numbers))
print(output)



#MAP WITH MULTIPLE ITERABLES
num1=[2,4,5]
num2=[4,6,3]

def sumUp(x,y):
    return x+y

output=list(map(sumUp,num1,num2))
print(output)