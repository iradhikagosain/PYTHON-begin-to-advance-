#CONDITIONAL STATEMENTS
age=int(input("enter age:"))

if age>18:
    print("have a license")
elif age==18:
    print("stay healthy")
elif age==0:
    print("sorry")
else:
    print("idk what to say")


#MATCH CASE
status=int(input("enter status:"))
match status:
    case 200:
        print("success!")
    case 404:
        print("not found")
    case 405:
        print("bad request")
    case _:
        print("Unknown status")    