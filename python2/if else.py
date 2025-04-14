#if-else
age=int(input("Enter your age:"))
if age>=18:
    print("You can drive")
else:
    print("You cannot drive")

#conditional statements
print(age>18)
print(age<18)
print(age>=18)
print(age<=18)
print(age==18)
print(age!=18) 
# Enter your age:18
# You can drive
# False
# False
# True
# True
# True
# False   

#if-else-elif
a=int(input("Enter a number:"))
if(a<0):
    print("The number is negative.")
elif(a==0):
    print("The number is zero.")
else:
    print("The number is positive.")