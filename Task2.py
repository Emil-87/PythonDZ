# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x1 = str (input('Enter X1:'))
y1 = int (input('Enter Y1:'))
x2 = int (input('Enter X2:'))
y2 = int (input('Enter Y2:'))


distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)
