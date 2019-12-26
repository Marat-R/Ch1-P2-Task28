# Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
# положительные - на число 1, ноль оставить без изменений.

list_a = [1,2,3,4,5,0,-1,-2,-3,-4,-5]
print(list_a)

def replace_items():
    for index, item in enumerate(list_a):
        if item > 0:
            list_a[index] = 1
        elif item < 0:
            list_a[index] = -1

replace_items()
print(list_a)

