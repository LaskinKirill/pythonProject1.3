import random
from random import randint
import shapely
from shapely.geometry import Polygon
import math

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

Al = []
for i in range(33):
    Al = alp[0: i]
    print(Al)

m = int(input('Введите число m '))
n = int(input('Введите число n '))
print(m, n)

A = [[pow(x + 1, y + 1) for x in range(m)] for y in range(n)]

for x in range(m):
    for y in range(n):
        print(A[x][y], end=' ')
    print()

print('Расчет площади пятиугольника.')
x1 = int(input('Введите x1 '))
x2 = int(input('Введите x2 '))
x3 = int(input('Введите x3 '))
x4 = int(input('Введите x4 '))
x5 = int(input('Введите x5 '))
y1 = int(input('Введите y1 '))
y2 = int(input('Введите y2 '))
y3 = int(input('Введите y3 '))
y4 = int(input('Введите y4 '))
y5 = int(input('Введите y5 '))

points5 = (x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)

area = 0


def areaofpolygon(polygon, i):
    global area
    if i == 0:
        area = 0

    try:
        x1, y1 = polygon[i]
        x2, y2 = polygon[i + 1]
        area += (x1 * y2) - (x2 * y1)

    except IndexError as e:
        x1, y1 = polygon[0]
        x2, y2 = polygon[-1]
        area += (x2 * y1) - (x1 * y2)
        return abs(area / 2.0)

    return areaofpolygon(polygon, i + 1)


def xrange(param):
    pass


def main():
    mypolygon = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
    print(mypolygon)

    area = areaofpolygon(mypolygon, 0)
    assert area == Polygon(mypolygon).area

    print('Площадь равна ', area, 'единицам.')
    return 0


if __name__ == '__main__':
    main()

print('Перевод римских цифр в арабские ')
integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def roman_to_arabic(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and integers[roman[i]] < integers[roman[i + 1]]:
            result -= integers[roman[i]]
        else:
            result += integers[roman[i]]
    return str(result)


roman1 = input('Введите римское число ')
arabic1 = roman_to_arabic(roman1)
print('Это арабское число - ', arabic1)

print('Тысяча бросков двух кубиков.')
One = "Кубик1"
Two = "Кубик2"

Sc1 = 0
Sc2 = 0
Sc3 = 0
Sc4 = 0
Sc5 = 0
Sc6 = 0
Sc7 = 0
Sc8 = 0
Sc9 = 0
Sc10 = 0
Sc11 = 0


for i in range(1000):

    FN = random.randint(1, 6)
    SN = random.randint(1, 6)
    Sum = FN + SN
    if Sum == 2:
        Sc1 += 1
    elif Sum == 3:
        Sc2 += 1
    elif Sum == 4:
        Sc3 += 1
    elif Sum == 5:
        Sc4 += 1
    elif Sum == 6:
        Sc5 += 1
    elif Sum == 7:
        Sc6 += 1
    elif Sum == 8:
        Sc7 += 1
    elif Sum == 9:
        Sc8 += 1
    elif Sum == 10:
        Sc9 += 1
    elif Sum == 11:
        Sc10 += 1
    elif Sum == 12:
        Sc11 += 1

print('2 выпало ', Sc1, 'раз.')
print('3 выпало ', Sc2, 'раз.')
print('4 выпало ', Sc3, 'раз.')
print('5 выпало ', Sc4, 'раз.')
print('6 выпало ', Sc5, 'раз.')
print('7 выпало ', Sc6, 'раз.')
print('8 выпало ', Sc7, 'раз.')
print('9 выпало ', Sc8, 'раз.')
print('10 выпало ', Sc9, 'раз.')
print('11 выпало ', Sc10, 'раз.')
print('12 выпало ', Sc11, 'раз.')
