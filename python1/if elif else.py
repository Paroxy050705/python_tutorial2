#wap to check if a number entered by the user is odd or even
num=int(input("Enter a number:"))
if(num%2==0):
    print("The num is even")
else:
    print("The num is odd")

#wap to find the graetest of 3 numbers by the user
n1=int(input("Enter 1st num:"))
n2=int(input("Enter 2nd num:"))
n3=int(input("Enter 3rd num:"))
if(n1>n2 and n1>n3):
    print("The 1st num is highest")
elif(n2>n1 and n2>n3):
    print("The 2nd num is highest") 
else:
    print("3rd num is highest")

#wap to check if a number is a multiple of 7 or not
num=int(input("Enter a number:"))
if(num%7==0):
    print("The  number is multiple of 7")
else:
    print("The number is not a multiple of 7")    


#wap to find the greater num
n1=int(input("Enter 1st num:"))
n2=int(input("Enter 2nd num:"))
n3=int(input("Enter 3rd num:"))
if(n1>n2):
    if(n1>n3):
        print("1st num is greater")
    else:
        print("3rd num is highest")
elif(n2>n1):
    if(n2>n3):
        print("2nd num is highest")
    else:
        print("3rd num is highest")
elif(n3>n1):
    if(n3>n2):
        print("3rd num is higher")
    else:
        print("2nd num is higher") 
else:
    print("Same")                                       