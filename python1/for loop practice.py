#print the elements of list using a loop
list=[1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)


#search for a num x in tuple
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number(1,4,9,16,25,36,49,64,81,100):"))
for i in tup:
    if(x==i):
        print("Found",x)
        break
    print(i)    



#wap to find the sum of first n numbers using while
n=int(input("Enter starting value:"))
p=int(input("Enter ending value:"))
i=1
s=0
while(i<=n):
    s=s+i
    i=i+1
print(s)    

n=int(input("Enter starting value:"))
p=int(input("Enter ending value:"))
s=0
for i in range(n,p+1):
    s=s+i
print("sum in between",n,"and",p,"is",s)    