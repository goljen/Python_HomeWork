# Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("Введите натуральное число: "))
for count in range(number):
    if  count != 0:
        product_numbers.append(product_numbers[count - 1] * (count + 1))
    else:
        product_numbers = [count + 1]
           
print('Набор произведений чисел от 1 до %d :'%(number), product_numbers)     