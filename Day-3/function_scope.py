"""def sum(a,b):
    c=a+b
    h=78
    return c


print(sum(5,3))
print(c)#local variable
"""



def sum(a,b):
    print("lets add")
    c=a+b
    global z #modifying z
    z=67#this will be the reffereed value
    return c

z=35
print((sum(46,3)))
print(z)