# # Задача 2
# # напишите код, которы принимает список из чисел и возвращает только сумму положительных чисел в нем.

# # Например,
# [1,-4,7,12] -> 1 + 7 + 12 = 20


primes = [1, -4, 7, 12]

# # Вариант 1 - с while
i = 0
total = 0
while i < len(primes):
    if primes[i] >= 0:
        total += primes[i]
    i += 1

print(total)

# Вариант 2 - c for
total = 0
for elem in primes:
    if elem >= 0:
        total += elem
print(total)



# Вариант 3 - индексы c for
# Генерация последовательности чисел
# print(list(range(1000, 10000)))

total = 0
for ind in range(len(primes)):
    if primes[ind] >= 0:
        total += primes[ind]    

print(total)



# Вариант 4 - функция enumerate()
total = 0
for ind, elem in enumerate(primes):
    print('Позиция элемента:', ind, 'Элемент:', elem)
    if elem >= 0:
        total += elem
print(total)
