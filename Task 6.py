import random
x = int(random.uniform(1, 1000))
y = int(random.uniform(1, 1000))
z = int(random.uniform(1, 1000))
print (x,y,z)
COST = (x+y+z)-1
def sum(x,y,z,COST):
    s1 = COST - x - y
    s2 = COST - x - z
    s3 = COST - y - z
    w = min(s1,s2,s3)
    if s1 == w:
        print (x,y, COST)
    if s2 == w:
        print (x, z, COST)
    if s3 == w:
        print (y,z, COST)
    return
sum(x,y,z,COST)