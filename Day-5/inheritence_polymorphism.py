class animal:
    location="india"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("speaking nowww....")


class dog(animal):#inheritence
    def speak(self):
      print("bow bow")


class cat(animal):
    def speak(self):
        print("meow")
        return super().speak()



#super() works when u want to use the function from parent class to child class
#Polymorphism, as we saw with the speak() method in the inheritance example, 
# means that objects of different classes can respond to the same method call in their own specific way. 
# This allows you to write code that can work with objects of different types without needing to know their exact class.
a=animal("dog")
a.speak()


d=dog("orio")
print(d.location)
print(d.name)
d.speak()

c=cat("kittu")
print(c.location)
print(c.name)
c.speak()




