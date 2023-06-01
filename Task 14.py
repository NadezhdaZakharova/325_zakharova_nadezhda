n = input("Введите имя: ")
import random 
g = random.randint(1, 100)
trick = input("Загадано число от 1 до 100")
kol = 0
while True:
    num = int(input("Введите число"))
    kol = kol +1

    if g>num:
        print("Подсказка: данное число меньше верного ответа")
    if g<num:
        print("Подсказка: это число больше верного ответа")
    if g==num:
        print("Верно!")
        with open("C:\\Users\\Надежда\\Documents\\GitHub\\125_zakharova_nadezhda\\game.txt","a") as f:
            f.write(f"\n{n}, you got nimber for {kol} steps!.\n Answer - {g}\n")
            break