def calc_sum(a,b): #here a,b are parameters &this is definition of function
    s=a+b
    print(s)
    return s
calc_sum(2,3)   #2,3 are arguments #this is calling
calc_sum(10,5)
calc_sum(88,89)


#avg of 3 numbers
def avg_num(a,b,c):
    s=(a+b+c)
    avg=s/3
    print(avg)
    return avg
a=int(input("Enter a number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
avg_num(a,b,c)    