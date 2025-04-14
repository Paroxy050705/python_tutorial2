#write a recursion function to calculate the sum of n natural numbers
n=int(input("Enter a number:"))
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
      return sum(n-1)+n
print(sum(n))



#write a recursive function to print all elements in a list
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruit=["Mango","litchi","apple","banana"]  
print_list(fruit) 