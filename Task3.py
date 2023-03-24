import random
List_1 = []
List_2 = []
for i in range(50,101):
    List_1.append(random.randint(0,10000))
    List_2.append(random.randint(0,10000))
Result = []
for k in List_1:
    if k in List_1 and k in List_2:
      Result.append (k)
print (Result)
