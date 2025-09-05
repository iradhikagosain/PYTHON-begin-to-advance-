#The constructor's job is to initialize the object's attributes – to give them their starting values. It sets up the initial state of the object.
class student:
    def __init__(self,name,uno):
        self.name=name
        self.uno=uno
    
    def  get_info(self):
        print(f'my name is {self.name} and university roll no. is {self.uno}')

s1=student("radhika",2329018)
print(s1.name)
print(s1.uno)
print(s1.get_info())


class animal:
    def __init__(self,name="dog",voice="boww bow"):
        self.name=name
        self.voice=voice


cat=animal("cat","meow meow")
kutta=animal()
print(cat.name,cat.voice)
print(kutta.name,kutta.voice)
        


