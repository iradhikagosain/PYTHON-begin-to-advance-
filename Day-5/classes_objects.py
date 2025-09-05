class Employee:#class
    company="HP"

    def get_salary(self):
        #self refers to the object of the class being created
        print(self)
        return 34000
    

e=Employee()#object of class employee
print(e.get_salary())
print(e.company)

e1=Employee()
print(e1.get_salary())


