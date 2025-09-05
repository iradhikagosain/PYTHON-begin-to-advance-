class employee:
    jobType="pvt job"#class attribute

    def __init__(self,name,department,jobType):
        self.name=name
        self.department=department
        self.jobType=jobType#instacnce attribute

e1=employee("radhika","developer","govt")
print(e1.jobType)
print(employee.jobType)


#object INTROSPECTION
print(dir(e1))