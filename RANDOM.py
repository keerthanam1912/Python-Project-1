import random
import string
n=int(input("Number of passwords you required:"))
length=int(input(f"Enter the length of all {n} passwords:"))
x=0
while(n>=x):
    low=string.ascii_lowercase
    upp=string.ascii_uppercase
    dig=string.digits[1:]
    sym=["!","@",'#','$']
    tot=random.choice(low)+random.choice(upp)+random.choice(sym)+random.choice(dig)
    a=''
    for i in range(length-4):
        a+=random.choice(dig)
    print(f"Your Password is:{a+tot}")
    x+=1
