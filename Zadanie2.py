#!/usr/bin/evn python3
# -*- config: utf-8 -*-

#Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
#которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
#вычисляющая площадь круга по формуле . В теле cylinder() у пользователя
#спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
#которая вычисляется по формуле , или полную площадь цилиндра. В последнем
#случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
#вычислений функции circle().

import math

def cylinder(r, h, full=True):
    def circle(r):
        return math.pi * (r ** 2)

    s_bor_cylinder = 2 * math.pi * r * h

    if full:
        return s_bor_cylinder + 2 * circle(r)
    else:
        return s_bor_cylinder

if __name__ == '__main__':
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    c = input("s_bor_cylinder(площадь боковой поверхности) или full(полная площадь)?")
    s = cylinder(r, h, full=(c == 'full'))
    print(s)