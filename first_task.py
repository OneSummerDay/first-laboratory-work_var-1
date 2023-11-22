#Лабораторна робота №1. Обробка послідовностей на мові Python. Рядки.
#Списки. Кортежі.

#Варіант 1

#Завдання 1


numbers = []

while True:
    try:
        user_input = int(input("Введіть ціле число (або 0 для завершення): "))
        if user_input == 0:
            break
        numbers.append(user_input)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

numbers.sort()

print("Введені числа у порядку зростання:")
for num in numbers:
    print(num)
