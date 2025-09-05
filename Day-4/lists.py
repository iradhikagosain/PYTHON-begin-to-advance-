''' DATA STRUCTURES IN PYTHON 
1. LISTS
'''
names=['radhika','diksha','mahi','mayank','richa','mahi']
marks=[35,32,22,43,46]
cgpa=[7.6,9.0,8.9,6.5,8.99]
student=['riya',45,9.8]
print(type(names))
print(type(marks))
print(type(cgpa))
print(type(student))


print(student[1])
print(names)
names[0]='radhika gosain'
print(names)

#list methods
student.append('jalandhar')
print(student)
student.insert(0,'mihir')
print(student)
student.remove('riya')
print(student)
student.pop()
print(student)
student.reverse()
print(student)


marks.sort()
print(marks)


#LIST COMPREHENSION
squared=[x**2 for x in range(1,11)]
print(squared)