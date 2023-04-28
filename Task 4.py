from random import randint
length = randint (5, 100)
a = [0] * length
for i in range (length):
    a[i] = randint(0, 9999)
x = randint(1, 1000000)
def magic (length, a, x):
    k = sum (a) % x
    if k == 0:
        return True
    else:
        return False
bool = magic (length, a, x)
print (bool)
