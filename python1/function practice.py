#wap to print the length of a list(list is the psrsmeter)
cities=["delhi","pune","mumbai","chennai","gurgaon","noida"]
cartoon=["shinchan","doreamon","chota bheem","dora","oggy"]
def print_len(list):
    print(len(list))
    print(list)
print_len(cities)  
print_len(cartoon) 


#wap to print the elements of a list in a single line
cities=["delhi","pune","noida","mumbai"]
def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(cities) 
#delhi pune noida mumbai

print(end="\n")
#write a function to find the factorial of n(n is the parameter)
n=int(input("Enter a number:"))
def fact(p):
    f=1
    for i in range(1,p+1):
        f=f*i
    print(f)  

fact(n)      
    

#waf to convert usd to inr
# 1 usd =83 inr
def converter(usd):
    inr=usd*83
    print("USD Value:",usd,"INR Value:",inr) 
usd=int(input("Enter USD value:"))
converter(usd)    



#wap to input a number through keyboard if the num is even print EVEN & if the num is odd then print ODD
n=int(input("Enter a number:"))
def cal_num(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
cal_num(n)            