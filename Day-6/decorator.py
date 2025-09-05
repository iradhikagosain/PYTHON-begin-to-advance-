def decorator(func):
    def wrapper():
        print("writing something...")
        func()
        print("already wrote")
    return wrapper

@decorator
def say_hello():
    print("hi everyone!")

#f=decorator(say_hello)
#f()
say_hello()