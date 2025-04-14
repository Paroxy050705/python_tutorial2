#create class
class Student:  #class name start with capital letter
    name="Karan"
#create object    
s1=Student()
print(s1.name)    #Karan
s2=Student()
print(s2.name)   #Karan



class Car:
    color="Blue"
    brand="Mercedes"
car1=Car()
print(car1.color)   
print(car1.brand)


#__init function__
class Student:
    name="Karan"
    def __init__(self):
        print("adding new student")
        print(self)   #<__main__.Student object at 0x000001B734876CF0>

s1=Student()



class Student:
    def __init__(self,name,marks,roll):
        print("welcome everyone")
        self.name=name
        self.marks=marks
        self.roll=roll
       
s1=Student("Karan",98,1)
print(s1.name,s1.marks,s1.roll) 

s2=Student("Arjun",95,2)
print(s2.name,s2.marks,s2.roll)

# welcome everyone
# Karan 98 1
# welcome everyone
# Arjun 95 2


#normal method
class Student:
    def college(self):
        print("hello")
s1=Student()
s1.college()        

#static method
class Student:
    @staticmethod
    def college():
        print("how are you")
s1=Student()
s1.college()        