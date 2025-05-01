# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
Things=input('Напишите числа(через пробел):')
K=Things.split()
Keys=[]
for i in K:
    Keys.append(int(i))
Values=[]
for el in Keys:
    if el%2==0:
        el='четное'
        Values.append(el)
    else:
        el='нечетное'
        Values.append(el)
dictionary=dict(zip(Keys,Values))
print(dictionary)
