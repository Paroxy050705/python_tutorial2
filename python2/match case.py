x=int(input("Enter an integer value of x:"))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is",x)        