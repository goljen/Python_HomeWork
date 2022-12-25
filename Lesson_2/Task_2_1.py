# Программа, которая принимает на вход вещественное число и показывает сумму его цифр

summ_digit = 0

number = list(input("Введите вещественное число: "))
for symbol in number:
    if  symbol == '-' or symbol == ',' or symbol == '.':
        summ_digit += 0
    else:
        summ_digit += int(symbol)
print('Сумма цифр введённого числа = ', summ_digit)     
