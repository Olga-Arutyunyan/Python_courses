import base64

def cut_square(a, b, counter):
    if a == b:
        if a == 1 or a % 2 != 0:
            return a
        if a % 2 == 0:
            counter += 1
            print_square(a // 2, b // 2, counter)
            return cut_square(a // 2, b // 2)
    if a < b:
        print("Максимальный квардрат:")
        counter += 1
        print_square(a, a, counter)
        print("Остаток от прямоугольника:")
        print_square(a, b - a, counter)
        return cut_square(a, b - a, counter)
    if a > b:
        print("Максимальный квардрат:")
        counter += 1
        print_square(b, b, counter)
        print("Остаток от прямоугольника:")
        print_square(a - b, b, counter)
        return cut_square(a - b, b, counter)


def print_square(a, b, counter):
    arr = [[get_base64_char(counter)] * b for i in range(a)]  # a - строки , b - столбцы
    for i in range(a):
        for j in range(b):
            print(arr[i][j], end=' '),
        print()
    print("___________________")

def get_base64_char(n):
    base64_arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if n < 64:
        return base64_arr[n]
    else:
        return base64_arr[n-64]

# начальные значения
a = 11
b = 8

counter = 0
print("Исходный прямоугольник:")
print_square(a, b, counter)
cut_square(a, b, counter)
