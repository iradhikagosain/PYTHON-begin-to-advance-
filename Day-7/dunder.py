class student:
    department="cse"
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def __str__(self):
        return f"the name of student is {self.name} and roll no. is {self.rno}"
    def __repr__(self):
        return f"name:{self.name} \n rno {self.rno}"
    def __len__(self):
        return len(self.name)

e=student("radhika",2329018)
print(e.name,e.rno)
print(str(e))
print(repr(e))
print(len(e))


class vectors:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return(self.x-other.x,self.y-other.y)
    
v1=vectors(23,6)
v2=vectors(26,8)
v3=v1+v2
print(v3)
v4=v1-v2
print(v4)