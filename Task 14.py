n = input("Введите имя: ")
import random 
g = random.randint(1, 100)
ima = input("Загадано число от 1 до 100")
kol = 0
while True:
    num = int(input("Введите число"))
    kol = kol +1

    if g>num:
        print("Подсказка: данное число больше верного ответа")
    if g<num:
        print("Подсказка: это число меньше верного ответа")
    if g==num:
        print("Верно!")
        with open("game.txt","a") as f:
            f.write(f"\n{ima}, вы угадали число за {kol} попыток!.\n Верный ответ - {g}\n")
            break