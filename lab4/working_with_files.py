# Вариант 4. Скопировать из файла F1 в файл F2 все строки, которые не содержат цифры.
# Подсчитать количество строк, которые начинаются на букву «А» в файле F2.

import os

def contains_digits(line):
    digits = "0123456789"
    for i in digits:
        if line.find(i) >= 0:
            return True
    return False

def count_of_A(array):
    count = 0
    for i in array:
        if i.startswith("A"):
            count += 1
    return count

try:
    F1 = open('F1.txt', 'r')
    print("File 'F1.txt' successfully opened.")
    result = []
    for line in F1:
        if contains_digits(line) == False:
            result.append(line)
    F1.close()
    print("File 'F1.txt' closed.")
    F2 = open('F2.txt', 'w')
    F2.writelines(result)
    F2.close()
    print("File 'F2.txt' closed.")
    print("In the output file 'F2.txt' " + str(count_of_A(result))+ " line(s) start(s) with 'A'. ")

except:
    print("File 'F1.txt' does not exist.")