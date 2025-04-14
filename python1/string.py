name="Tony Stark"
print(name.upper()) #TONY STARK
print(name.lower())  #tony stark
print(name.find('y'))  #3
print(name.find('H'))  #-1
print(name.find("Stark"))  #5  (starts from index 5)
print(name.find("stark"))  #-1  (because small 's' is absenrt so it returns -1)
print(name.replace("Tony Stark","Ironman"))  #Ironman
print(name)  #Tony Stark(it dose not change the original string)
print(name.replace('T','Y'))  #Yony Stark
print('o' in name)  #True
print('x' in name)  #False
a=12
b=5
c=a//b
print(c)