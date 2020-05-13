"""Вариант 10. Создать класс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
 Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
 Создать список объектов. Вывести:
 a)	список автомобилей заданной марки;
 b)	список автомобилей заданной модели, которые эксплуатируются больше n лет; """

import datetime

def current_year():
   today = str(datetime.date.today())
   current_year = int(today[0] + today[1] + today[2] + today[3])
   return current_year

class Car:
    __id = 0
    __mark = ""
    __model = ""
    __production_year = 0
    __color = ""
    __price = 0
    __reg_number = ""

    def __init__(self, id, mark, model, production_year, color, price, reg_number):
        self.__id = id
        self.__mark = mark
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__price = price
        self.__reg_number = reg_number

    def __str__(self):
        return str(self.__id) + " " + str(self.__mark) + " " + str(self.__model) + " " \
               + str(self.__production_year) + " " + str(self.__color)  \
                + " " + str(self.__price) + " " + str(self.__reg_number)

    def get_id(self):
        return self.__id

    def get_mark(self):
        return self.__mark

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_reg_number(self):
        return self.__reg_number

    def set_id(self, id):
        if type(id) == "int":
            if 0 < id <= 999999:
                self.__id = id
        else:
            print("Значение параметра ID '" + str(id) +
                  "' некорректно. Используйте целое число от 0 до 999999. ")

    def set_mark(self, mark):
        if mark != "":
            self.__mark = mark
        else:
            print("Значение параметра mark '" + str(mark) +
                  "' некорректно. Данное поле не может быть пустым. ")

    def set_model(self, model):
        if model != "":
            self.__model = model
        else:
            print("Значение параметра model '" + str(model) +
                  "' некорректно. Данное поле не может быть пустым. ")

    def set_production_year(self, production_year):
        if type(production_year) == "int":
            if 1900 <= production_year <= 2020 :
                self.__production_year = production_year
        else:
            print("Значение параметра Production Year '" + str(production_year) +
                  "' некорректно. Используйте целое число от 1900 до 2020. ")

    def set_color(self, color):
        if color != "":
            self.__color = color
        else:
            print("Значение параметра color '" + str(color) +
                  "' некорректно. Данное поле не может быть пустым. ")

    def set_price(self, price):
        if type(price) == int:
            if 0 < price <= 999999:
                self.__price = price
        else:
            print("Значение параметра price '" + str(price) +
                  "' некорректно. Используйте целое число от 0 до 999999. ")

    def set_reg_number(self, reg_number):
        if reg_number != "":
            self.__reg_number = reg_number
        else:
            print("Значение параметра Registration number '" + str(reg_number) +
                  "' некорректно. Данное поле не может быть пустым. ")

    def get_age(self):
        return current_year() - self.get_production_year()

# код для проверки корректной работы методов get и set
"""new_car = Car(123456, "Opel", "Astra", 2007, "green", 8500, "1234RX1")
print(new_car)
new_car.set_color("black")
new_car.set_mark("")
new_car.set_production_year("ccc")
new_car.set_price("bbb")
new_car.set_price(14620)
new_car.set_id(987654)
print(new_car)
print(new_car.get_model())
print(new_car.get_production_year())"""


cars = [
    Car(123456, "Opel", "Astra", 2007, "green", 8500, "1234RX1"),
    Car(543890, "BMW", "X6", 2019, "black", 40000, "6666XX6"),
    Car(543890, "BMW", "X4", 2018, "white", 35000, "4444XX4"),
    Car(430098, "Renaut", "Sandero", 2015, "white", 7000, "5231BV3"),
    Car(845201, "Geely", "Atlas", 2018, "red", 15000, "9623WE5"),
    Car(548075, "Mercedes", "S-W220", 2001, "black", 3000, "8753AQ7"),
    Car(549241, "Kia", "Rio", 2010, "brown", 6200, "9811OI9"),
    Car(354023, "Mazda", "3", 2005, "gray", 6000, "6543BN7"),
    Car(756202, "Mazda", "626", 2000, "red", 3000, "9821DE5"),
    Car(123456, "Opel", "Insignia", 2019, "black", 10000, "6784ER3"),
    Car(729563, "Pegeut", "307", 1997, "blue", 2700, "6542YT8"),
]

# a : вывести список автомобилей заданной марки
selected_mark = input(("Введите марку машины для поиска: \n"))
found_selected_mark = False

for car in cars:
    if car.get_mark() == selected_mark:
        found_selected_mark = True
        print(car)
if not found_selected_mark:
    print("Машин данной марки в списке нет.")

# b : вывести список автомобилей заданной модели, которые эксплуатируются больше n лет
selected_mark = input(("Введите марку машины для поиска: \n"))
selected_model = input(("Введите модель машины для поиска: \n"))
use_time = int(input(("Введите количество лет эксплуатации для поиска: \n")))
found_matches = False

for car in cars:
    if car.get_mark() == selected_mark:
        if car.get_model() == selected_model:
            if car.get_age() > use_time:
                found_matches = True
                print(car)
if not found_matches:
    print("Не нашлось машин, удовлетворяющих параметрам поиска.")