class employee:
    company ="asus"
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print(f"name of employee is :{self.name}")
    @staticmethod#static methods doesn't need any self parameter
    def sum(a,b):
        return a+b
    @classmethod#change class attributes take cls as first parameter
    def change(cls):
        print(cls.company)
    @classmethod
    def change_company(cls,new):
        cls.company=new
        print(cls.company)
    

e=employee("radhika")
e2=employee("kashish")
print(e.company)
print(e.name)   
print(employee.company)
#print(employee.name) 
e.get_info()
e2.get_info()
#employee.get_info()
print(e.sum(34,2))
#class method
print(employee.company)
e.change()
e.change_company("hppp")
print(employee.company)


