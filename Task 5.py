import random
#a=(random.uniform(1000,99999))
#b=(random.uniform(1000,99999))
a = 1001.25
b = 2002.37760505
c=float(a+b)

def eqv(a, b, c):
    if a<b:
        eps=0.0001*b
    else:
        eps=0.0001*b   
    if eps > abs(c - a - b):
        return True
    else:
        return False

print (eqv(a,b,c))
print (a,b,c)

