first_num=int(input("Enter 1st number:"))
second_num=int(input("Enter 2nd number:"))
operator=input("Select operators(+,-,*,/,**,%,//):")
if operator=="+":
    sum=first_num+second_num
    print("The sum of",first_num,"&",second_num,"is",str(sum))
elif operator=="-":
    subtraction=first_num-second_num
    print("The subtraction of",first_num,"&",second_num,"is",str(subtraction))
elif operator=="*":
    multiplication=first_num*second_num
    print("The multiplication of",first_num,"&",second_num,"is",str(multiplication))
elif operator=="/":
    division=first_num/second_num
    print("The division of",first_num,"&",second_num,"is",str(division))
elif operator=="**":
    a=first_num**second_num
    print("The exponential of",first_num,"&",second_num,"is",str(a))
elif operator=="%":
    b=first_num%second_num
    print("The modulus of",first_num,"&",second_num,"is",str(b))
elif operator=="//":
    c=first_num//second_num
    print("The floor division of",first_num,"&",second_num,"is",str(c))
else:
    print("You entered a wrong operator.Please enter 1 operator only from these +,-,*,/,**,%,// operators...")