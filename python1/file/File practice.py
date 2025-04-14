#crete a new file "practice.txt" using python.add data.
f=open("Python 1 shot by apna college/file/practice.txt","w")
f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java.")
f.close()

#waf that replaces all occurence of "Java" with "Python"
f=open("Python 1 shot by apna college/file/practice.txt","r")
data=f.read()
print(data)
new=data.replace("Java","Python")
print(new)
f=open("Python 1 shot by apna college/file/practice.txt","w")
f.write(new)
f.close()

#wap to find "learning"
def check_word():
    f=open("Python 1 shot by apna college/file/practice.txt","r")
    info=f.read()
    print(info)
    if(info.find("learning")!=-1):
        print("found")
    else:
        print("not found") 
check_word()
def check_line():
    f=open("Python 1 shot by apna college/file/practice.txt","r")
    info=f.readline()           