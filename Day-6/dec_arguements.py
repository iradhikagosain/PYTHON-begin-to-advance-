def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator    


@repeat(10)
def greet(name):
    print(f"hello!,{name}")    

greet("radhika")