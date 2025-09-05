#printing fibonacci series using recursiion

def fibo(n):
    if(n==0 or n==1):
        return n
    
    return fibo(n-2)+fibo(n-1)

print(fibo(7))


#printing factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120