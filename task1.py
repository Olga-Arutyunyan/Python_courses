# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

n = int(input("Введите натуральное четырехзначное число n: \n"))
# проверка правильности ввода
if (n // 1000 == 0) or (n // 1000 >= 10) or (n <= 0):
    print("Введенное число не соответствует требованиям.")
else:
# представим n в виде abcd
    a = n // 1000
    b = n // 100 % 10
    c = n % 100 // 10
    d = n % 10
    if (a==b) or (a==c) or (a==d) or (b==c) or (b==d) or (c==d):
        print ("Данное число содержит одинаковые цифры.")
    else:
        print("Все цифры данного числа различны.")


