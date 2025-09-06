def less_than_8(i):
    if(i<8):
        return True
    else:
        return False


nums=[24,7,2,52,-3,6.-5,-6,-1,3,577,3,-2,2]
#output=list(filter(less_than_8,nums))
#print(output)

output=list(filter(lambda i:i>8,nums))
print(output)