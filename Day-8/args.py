def sum(a,b):
    return a+b

print(sum(24,6))


#args will be a tuple of all the values passed to mul
def mul(*args):
    print(args)
    m=1
    for i in args:
        m*=i
    
    return m


print(mul(34,6,9,89,3,5,46,4,3))