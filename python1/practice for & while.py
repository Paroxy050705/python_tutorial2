#wap to find the sum of first n numbers using while
n=int(input("Enter ending value:"))
i=1
s=0
while(i<=n):
    s=s+i
    i=i+1
print("Sum of 1 to",n,"is:",s)    

n=int(input("Enter starting value:"))
p=int(input("Enter ending value:"))
s=0
for i in range(n,p+1):
    s=s+i
print("sum in between",n,"and",p,"is",s)    


#factorial
n=int(input("Enter a number:"))
f=1
for i in range(1,n+1,1):
    f=f*i
    i=i+1
print("Factorial of",n,"is:",f)

n=int(input("Enter a number:"))
f=1
i=1
while(i<=n):
    f=f*i
    i+=1
print(f)    