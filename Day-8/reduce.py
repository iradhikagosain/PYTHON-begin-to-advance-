from functools import reduce
nums=[35,3,6,3,7,3,67,4,3,675]


def sum(a,b):
    return a+b

c=reduce(sum,nums)
print(c)

result = reduce(lambda x, y: x + y, nums, 10)
print(result) 