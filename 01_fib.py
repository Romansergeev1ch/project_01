# Оператор цикла for - перебирает элементы в коллекции
# примение break, continue
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

for price in room_prices:
    if price == max(room_prices):
        continue
    if price == min(room_prices):
        print('Минимальная цена:', price)
        break
    print('Текущая цена:', price)

print('До свидания!')







# Задача 1: Последовательность Фибоначи
# Чему равен 100 элемент?
# 1 2 3 4 5 6    100
# 1 1 2 3 5 8     ?

fib1, fib2 = 1, 1

n = input('Номер элемента ряда Фибоначчи: ')

# Вариант 1 - через цикл whille
i = int(n) - 2

while i > 0:
    print(fib2)
    fib1, fib2 = fib2, fib1+ fib2
    i -= 1

print('Значение этого элемента: ', fib2)


# Вариант 2 - через цикл for

for i in range(2, int(i)):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2)
