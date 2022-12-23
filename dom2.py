# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .


x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

a = x * y * z
b = x + y + z

if a > 0:
 a = 0
elif a < 1:
 a = 1
if b > 0:
 b = 1
elif b < 1:
 b = 1

if a == b:
     print('Утверждение истинно')
elif a != b:
    print('Утверждение ложно')

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
  print('Утверждение истинно')
else:
  print('Утверждение ложно') 
#fd