first=int(input("Enter 1st number:"))
second=int(input("Enter 2nd number:"))
operator=input("Enter operator(+,-,*,/,//,**,%):")
if operator=='+':
    sum=first+second
    print("Answer is:"+str(sum))
elif operator=='-':
    subtract=first-second
    print("Answer is:"+str(subtract))
elif operator== '*':
    multiply=first*second
    print("Answer is:"+str(multiply))
elif operator== '/':
    division=first/second
    print("Answer is:"+str(division))
elif operator=='//':
    a=first//second
    print("Answer is:"+str(a))
elif operator=='**':
    b=first**second
    print("Answer is:"+str(b))
elif operator=='%':
    c=first%second
    print("Answer is:"+str(c))
else:
    print("You entered wrong operator")
