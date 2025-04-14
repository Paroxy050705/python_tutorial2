#create student class that takes name & marks of 3 subjects are arguments in constractor.Then create a method to print the average.

#create class
class Student:
    def __init__(self,name,marks):#constractor
        self.name=name #obj attribute
        self.marks=marks
        
    def avg(self): #methods
        sum=0
        for val in self.marks:
            sum=sum+val
            avg=sum/3
        print("Hi",self.name,"Your total score is",sum,"avg score is",avg)


#create object
s1=Student("Tony stark",[98,99,100])
s1.avg()




#create Account class with 2 attributes balance & account no.create methods for debit,credit,printing the balance.
class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    def debit(self,amount):
        self.bal-=amount
        print("Rs",amount,"was debited")
        print("Total balance=",self.print_bal())
    def credit(self,amount):
        self.bal=self.bal+amount
        print("Rs",amount,"was credited")  
        print("Total balance=",self.print_bal())
    def print_bal(self):
        return self.bal    
acc1=Account(10000,1234)
acc1.debit(1000)
acc1.credit(500)



#to  add 2 numbers
class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add_num(self):
        return self.a+self.b
            
a1=Add(4,3) 
print(a1.add_num())


#define a circle class to create a circle with radius r using the constractor.define an area() method which calculate area & perimeter() method which calculate perimeter.
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return (22/7)*self.r*self.r
    def perimeter(self):
        return 2*(22/7)*self.r
c1=Circle(21)
print(c1.area())
print(c1.perimeter())



#define a employee class with attributes role,department,salary.this class also have showdetails() method.
class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showdatils(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.sal)


class Engineer(Employee):#Inherits property from employe
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("enginner","it",6789000)
eng1=Engineer("elon musk",40)
eng1.showdatils()            