name="Paramita"
for i in name:
    print(i)
# P
# a
# r
# a
# m
# i
# t
# a    

#loop in list
list=["Mango","Apple","Litchi","Guava","Pinaple"]
for i in list:
    print(i)
# Mango
# Apple
# Litchi
# Guava
# Pinaple    

colours=["Red","Green","Blue","Pink","Yellow"]
for j in colours:
    print(j)
    for i in j:
       print(i)   
# Red
# R
# e
# d
# Green
# G
# r
# e
# e
# n
# Blue
# B
# l
# u
# e
# Pink
# P
# i
# n
# k
# Yellow
# Y
# e
# l
# l
# o
# w        

for k in range(5):
    print(k)
# 0
# 1
# 2
# 3
# 4   
for k in range(5):
    print(k+1)
# 1
# 2
# 3
# 4
# 5   
for k in range(1,9):
    print(k)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8    
for k in range(5,0,-1):
    print(k)
# 5
# 4
# 3
# 2
# 1   
for k in range(1,8,2): #here 1=starting parameter,8=ending parameter,2=gap
    print(k)
# 1
# 3
# 5
# 7    