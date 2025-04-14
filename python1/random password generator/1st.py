import random
import string


# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
charValues=string.ascii_letters+string.digits+string.punctuation

pass_len=int(input("Enter your password length:"))
password=""
for i in range(pass_len):
    password=password+random.choice(charValues)
print("Your random password is:",password)