student={
    "name":"radhika",
    "age":23,
    "cgpa":8.9,
    
}

print(type(student))
print(student)
print(student["name"])
student["age"]=30
print(student)
student["address"]='jalandhar'
print(student)

#dict methods
print(student.keys())
print(student.values())
print(student.items())

student.pop('address')
print(student)
student.clear()
print(student)