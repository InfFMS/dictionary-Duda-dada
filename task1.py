# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
from numpy.ma.core import append

Things=input('Напишите предметы(через пробел):')
Count=input('Напишите количество кажого из предметов соотвественно(через пробел):')
Keys=Things.split()
Value=Count.split()
Values=[]
for el in Value:
    Values.append(int(el))
dictionary=dict(zip(Keys,Values))
print(dictionary)