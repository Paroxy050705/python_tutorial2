#strings are immutable
a="Harry"
print(a)

#upper()  & lower()
print(a.upper())
print(a)  #main string does not change so the strings are immutable
print(a.lower())
print(a)  #main string does not change so the strings are immutable
# Harry
# HARRY
# Harry
# harry
# Harry

#rstrip(" ")
b="Harry!!!!!!!"
print(b)  #Harry!!!!!!!
print(b.rstrip("!"))  #Harry

c="!!!!Hello!!!!"
print(c.rstrip("!"))  #!!!!Hello

d="!!!!Hello!!!!1"
print(d.rstrip("!"))    #!!!!Hello!!!!1

#replace(" "," ")
e="!!hello!!"
print(e.replace("hello","hi"))  #!!hi!!

#split("")
f="!!! harry2 31!! hello!! !1"
print(f.split(" "))
print(f.split("!"))
# ['!!!', 'harry2', '31!!', 'hello!!', '!1']
# ['', '', '', ' harry2 31', '', ' hello', '', ' ', '1']

#capitalize()
h="heLLo guYS"
print(h.capitalize())   #Hello guys


#center()
x="Welcome to Python course"
print(len(x))  #24
print(x.center(60))  
#                  Welcome to Python course
print(len(x.center(60))) #60

#count("")
a="Hello I am Paramita.Paramita is my name."
print(a.count("Paramita"))  #2
print(a.count("a"))  #8

#endswith("")
u="Hello I am Paramita.Paramita is my name."
print(u.endswith("."))  #True
print(u.endswith("!"))   #False

v="Hello I am Paramita.Paramita is my name."
print(v.endswith("am",4,10))   #True

#find("")
str1="Hey I am here.Are you There?"
print(str1.find("am"))  #6
print(str1.find("us"))  #-1

#index()
str1="Hey I am here."
print(str1.index("am"))  #6
#print(str1.index("us"))  #value error

#isalnum()
s=" welcome to the console"
print(s.isalnum())  #False [because space is present here]
s="welcometotheconsole"
print(s.isalnum())  #True


#isalpha
s="welcome"
print(s.isalpha())  #True
s="welcome09"
print(s.isalpha())  #False


#islower()
s="hello World"
print(s.islower())  #False
s="hello world"
print(s.islower())  #True

#isprintable()
s="hello Welcome here."
print(s.isprintable())  #True
s="hello Welcome \n here."
print(s.isprintable())  #False  [here \n is present we can not print \n]

#isspace()
s="    "
print(s.isprintable())  #True
print(s.isspace())    #True


#istitle()
s="World Health Organization"
print(s.istitle())  #True
s="World health Organization"
print(s.istitle())  #False


#startswith()
a="Python is an interpereted language."
print(a.startswith("Python"))  #True

#swapcase()
a="Python is a Interpreted Language"
print(a.swapcase())  #pYTHON IS A iNTERPRETED lANGUAGE

#title()
a="His name is Dan.Dan is an honest man."
print(a.title())  #His Name Is Dan.Dan Is An Honest Man.
