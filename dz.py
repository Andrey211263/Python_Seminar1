# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#  Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
# day = int(input('Введите номер дня недели '))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')
# else:
#     print(f'Такого дня недели нет {day}')

# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
from subprocess import list2cmdline


list1 = [0, 0, 0]
list2 = [0, 0, 1]
list3 = [0, 1, 0]
list4 = [0, 1, 1]
list5 = [1, 0, 0]
list6 = [1, 0, 1]
list7 = [1, 1, 0]
list8 = [1, 1, 1]

def f(list):
    a = not(list[0] or list[1] or list[2])
    b = not list[0] and not list[1] and not list[2]
    print(f'{list} ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> {a} = {b}')
    # return
f(list1)
f(list2)
f(list3)
f(list4)
f(list5)
f(list6)
f(list7)
f(list8)



  # 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причем X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#  Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input('Введите координату х: '))
# y = int(input('Введите координату у: '))
# if x > 0 and y > 0:
#     print(f'I четверть -> {x}, {y}')
# elif x < 0 and y > 0:
#     print(f'II четверть -> {x}, {y}')
# elif x < 0 and y < 0:
#     print(f'III четверть -> {x}, {y}')
# elif x > 0 and y < 0:
#     print(f'IV четверть -> {x}, {y}')
# elif x == 0 and y > 0:
#     print('I - II четверть')
# elif x > 0 and y == 0:
#     print('I - IV четверть')
# elif x == 0 and y < 0:
#     print('III - IV четверть')
# elif x < 0 and y == 0:
#     print('II - III четверть')

# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))
# if quarter == 1:
#     print('I четверть: диапазон х: 0 +бесконечность, y: 0 +бесконечность')
# elif quarter == 2:
#     print('II четверть: диапазон х: 0 -бесконечность, y: 0 +бесконечность')
# elif quarter == 3:
#     print('III четверть: диапазон х: 0 -бесконечность, y: 0 -бесконечность')
# elif quarter == 4:
#     print('IV четверть: диапазон х: 0 +бесконечность, y: 0 -бесконечность')
# print('Такой четверти нет')



# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
#  Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# #from cmath import sqrt


# x1 = int(input('Введите координату первой точки х: '))
# y1 = int(input('Введите координату первой точки у: '))
# x2 = int(input('Введите координату второй точки х: '))
# y2 = int(input('Введите координату второй точки у: '))
# # leng = sqrt((x1-x2)**2 + (y1-y2)**2)
# # print(type(leng))
# leng = round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)
# print(f'Длина отрезка = {leng}')
