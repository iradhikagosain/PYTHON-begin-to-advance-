try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))

    print("1. for ADD\n"\
    "2. For SUB \n"\
    "3. For MUL\n "\
    "4. For div")
    o=int(input("enter operation:"))
    match o:
        case 1:
            print(f"result is {a+b}")
        case 2:
            print(f"result is {a-b}")
        case 3:
            print(f"result is {a*b}")
        case 4:
            print(f"result is {a/b}")
        case default:
            print("INVALID OPERATION")
except Exception as e:
    print("enter valid value!")