fruits={'apples','mangos','oranges','grapes','berries',46,7,2.5,6+4j,46}
#print(fruits[3])#can't be accessed
print(fruits)

#set methods
fruits.add('strwberry')
print(fruits)
fruits.remove(46)
print(fruits)
fruits.discard('grapes')
print(fruits)
fruits.pop()
print(fruits)


#set operations
a={1,2,3,4}
b={4,5,6,3}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))