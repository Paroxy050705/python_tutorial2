marks=[98,99,100]
for score in marks:
    print(score)
#98
#99
#100
    
marks.append(101)
print(marks)  #[98,99,100,101]
marks.insert(0,97)
print(marks)  #[97,98,99,100,101]
print(100 in marks)  #True
print(10 in marks)  #False 
print(len(marks)) #5 


set={1,2,3,4,5,1,2,4,5}
for i in set:
    print(i)  #1 2 3 4 5 

str="Paramita"
for char in str:
    print(char)
else:
    print("END")    
# P
# a
# r
# a
# m
# i
# t
# a
# END    