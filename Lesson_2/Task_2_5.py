# Программа реализует алгоритм перемешивания списка.

import random

# подпрограмма случайного перемешивания списка
def mix_list(list_original):  
    list_result = []               
    # Создаем копию, поскольку мы не должны изменять оригинал
    list_result = list_original[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list_result)
    for i in range(list_length):
        # Получение случайного индекса
        index_arbitrary = random.randint(0, list_length - 1)
        # Замена
        temp = list_result[i]
        list_result[i] = list_result[index_arbitrary]
        list_result[index_arbitrary] = temp
    # Возвращаем список
    return list_result
    
# подпрограмма создания списка
def create_list(list_members):
    list_original = []
    for i in range(list_members):
        list_original.append(i)
    return list_original


first_list = []
second_list = []
number = int(input("Введите натуральное число: "))
first_list = create_list(number)
print("Исходный список: ")
print(first_list)
second_list = mix_list(first_list) 
print("Перемешанный список: ")
print(second_list)