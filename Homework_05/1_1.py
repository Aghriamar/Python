# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a, -b)
    if b % 2 == 0:
        return power(a, b // 2) * power(a, b // 2)
    else:
        return power(a, b - 1) * a
print(f"Answer: {power(int(input('Input first number: ')), int(input('Input second number: ')))}")