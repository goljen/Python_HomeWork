# Программа принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

digit = int(input("Введите цифру обозначающую день недели (1-7): "))
if digit == 6 or digit == 7:
    print("Это выходной день!")
else:
    print("К сожалению это рабочий день.")