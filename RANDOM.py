import random
import string
low=string.ascii_lowercase
upp=string.ascii_uppercase
dig=string.digits[1:]
sym=["!","@",'#','$']
tot=random.choice(low)+random.choice(upp)+random.choice(sym)+random.choice(dig)
length=int(input("Enter Length Of Password:"))
a=''
for i in range(length-4):
    a+=random.choice(dig)
print(f"Your Password is:{a+tot}")

    

