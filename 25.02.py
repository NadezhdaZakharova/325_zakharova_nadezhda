import math
print ('Начало расчета')
G0 = 6.674*math.pow(10,-11)
M1 = 5.97600*math.pow(10,24)
print("Введите растоояние между объектами")
S = float(input())
print ('Введите массу выбранного объекта')
M2 = float(input())
print ('Введите cтепень 10 массы второго объекта: ')
mst=float(input())
M2=M2*math.pow(10,mst)
print ('Введите cтепень 10 расстояния до второго объекта: ')
rst=float(input())
S=S*math.pow(10,rst)
F=(G0*M1*M2)/(math.pow(S,2))
print (F)


