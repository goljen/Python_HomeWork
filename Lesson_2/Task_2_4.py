# Программа создает список, заполненных числами из промежутка [-N, N], N вводит пользователь
# и расчитывает произведение элементов на позициях, указанных пользователем.

import random

# подпрограмма создания списка
def create_list(list_members):
    list_original = []
    for i in range(-list_members, list_members + 1):
        list_original.append(i)
#        list_original.append(random.randint(- list_members, list_members))
    return list_original

new_list = []
# second_list = []
number = int(input("Введите натуральное число: "))
new_list = create_list(number)
print("Исходный список: ")
print(new_list)
first_position = int(input('Введите первое натуральное число от 0 до %d :'%(number * 2)))
second_position = int(input('Введите второе натуральное число от 0 до %d не равное первому :'%(number * 2)))
product_position = new_list[first_position] * new_list[second_position]
print('Произведение элементов во введенных позициях = ', product_position)