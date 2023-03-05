# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

def summa(a, b):
    if a < 0:
        a = -(a)
    if b < 0:
        b = -(b)
    if a == 0:
        return b
    return summa(a - 1, b + 1)
print(f"Answer: {summa(int(input('Input first number: ')), int(input('Input second number: ')))}")