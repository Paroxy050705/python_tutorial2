def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
n=int(input("Enter a number:"))
show(n)  


#wap to count factorial using recursion
n=int(input("Enter a number:"))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(n))    