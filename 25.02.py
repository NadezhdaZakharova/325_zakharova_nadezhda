import math
print ('Начало расчета')
def power(M2, S):
    G0 = 6.6743*(math.pow(10,-11))
    M1 = 5.97600 * math.pow(10,24)
    return (G0*M1*M2)/(math.pow(S,2))
print('Введите расcтояние между объектами')
S = float(input())
print ('Введите массу выбранного объекта')
M = float(input())
print ('Введите cтепень 10 массы второго объекта')
mst = float(input())
M2 = M*math.pow(10,mst)
F = power(M2,S)
print (F)


