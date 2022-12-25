# Программа, которая принимает на вход число N, формирует список 
# из n чисел последовательности (1+1/n)**n и выводит на экран список, словарь и сумму элементов.

summ_listitems = 0
list_items = []


number = int(input("Введите натуральное число: "))
for count in range(1, number + 1):
    element = 3 * count + 1
    summ_listitems += element
    list_items.append([count, element])
dict_items = dict(list_items)

print('Двухмерный список: ', list_items)          
print('Сумма элементов списка:', summ_listitems)  
print('Словарь из элементов списка: ', dict_items)   