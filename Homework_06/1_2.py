# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

nums_list = [int(i) for i in input().split]
num_min = int(input())
num_max = int(input())
print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])