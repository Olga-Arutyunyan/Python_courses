# 2. Все четные по значению элементы исходного списка A поместить в новый список B.

import random
n = int(input("Введите размер списка А: \n"))
A = []
B = []
for i in range(n):
    A.append(random.randint(0, 99))
    if A[i] % 2 == 0:
        B.append(A[i])
print("A: ", A)
print("B: ", B)


