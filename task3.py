# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к
Stroka=input('напишите любую строку:')
NormStroka=Stroka.lower()
dictionary={}
for i in NormStroka:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
#print(dictionary)
for key in dictionary:
    print(key, '-', dictionary[key],end=' ')

