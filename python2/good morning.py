time=int(input("Enter a time in 24 hours format:"))
if(time>=4 and time<12):
    print("Good morning")
elif (time>=12 and time<16):
    print("Good afternoon")
elif(time>=16 and time<20):
    print("Good evening")
else:
    print("Good night") 



import time
print("Current time:",time.strftime("%H:%M:%S"))
h=int(time.strftime("%H"))
if(h>=4 and h<12):
    print("Good morning")
elif (h>=12 and h<16):
    print("Good afternoon")
elif(h>=16 and h<20):
    print("Good evening")
else:
    print("Good night") 
