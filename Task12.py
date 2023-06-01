#a = int(input())
#b = int(input())
a = 3
b = 1
if a > b:
    start = b
    end = a
else:
    start = a
    end = b 

def sum_range(start, end):
    Y = 0
    for i in range(start, end+1):
        Y += i
    return (Y)
sum_range(start, end)
print (sum_range(start, end))