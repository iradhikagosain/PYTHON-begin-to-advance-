#ERROR HANDLING
while True:
    try:
        a=int(input("enter num 1:"))
        b=int(input("enter num 2:"))
        print(f"total sum is {a+b}")
    except:
        print("wrong value entered !")
        break


while True:
    try:
        c=int(input("enter num 3:"))
        d=int(input("enter num 4:"))
        print(f"total answer: is {c/d}")
    except ValueError:
        print("don't perform")
    except ZeroDivisionError:
        print("don't divide by zero")
    except Exception as e:
        print("some error occurred",e)


#RAISING ERRORS
a=int(input("enter num 1:"))
b=int(input("enter num 2:"))
if b==0:
    raise ValueError("don't perform operation with zero")
print(f"total sum is {a/b}")