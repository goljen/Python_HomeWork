# Программа по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

quadrant = int(input("Введите номер четверти: "))


while (quadrant < 1 or quadrant > 4):
    print("Не верно введён номер четверти!!!")
    print("Попробуйте ещё раз.")
    quadrant = int(input("Введите номер четверти: "))

if (quadrant == 1):
    print("Значение координат в четверти", quadrant, "X > 0 и Y > 0")
elif(quadrant == 2):
    print("Значение координат в четверти", quadrant, "X < 0 и Y > 0")
elif(quadrant == 3):
    print("Значение координат в четверти", quadrant, "X < 0 и Y < 0")
else:
    print("Значение координат в четверти", quadrant, "X > 0 и Y < 0")
