# Задача 2:
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите число: '))
num = number
sum = 0

while (num > 0):
    sum = sum + num % 10
    num = num // 10

print(f'Сумма цифр в числе {number} -> {sum}')
