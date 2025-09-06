def slow():
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    return 70

#without walrus
'''
a=slow()
if (a>10):
    print(a)
else:
    print("not greater than 10")

'''
#with walrus
if((a:=slow()>10)):
    print(a)