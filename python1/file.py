#read mode
f=open("Python 1 shot by apna college/file demo.txt","r")
data=f.read()
print(data)   #hello,I am learning python
print(type(data))
f.close()

f=open("Python 1 shot by apna college/file demo.txt","rt")
data2=f.read(3)  #hel
print(data2)
f.close()

f=open("Python 1 shot by apna college/file demo.txt","rt")
line1=f.readline()
print(line1)  #print only 1st line
f.close()

#write mode(overwrite)
f=open("Python 1 shot by apna college/file demo.txt","w")
f.write("I am human")
f.close()

#append mode(write something on last)
f=open("Python 1 shot by apna college/file demo.txt","a")
f.write(" & I LOVE CS")
f.close()


#special case
f=open("Python 1 shot by apna college/flow.txt","w")
f.write("Hi")
f.close()
#flow.txt file create kora chilo nah avabe direct create kora jai

f=open("Python 1 shot by apna college/fig.txt","a")
f.close()