# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

dict1={'a': 100, 'b': 200, 'c':300}
dict2={'a': 300, 'b': 200, 'd':400}
NormDict2={}
for el in dict2:
    NormDict2[el]=dict2[el]
for i in dict1:
    if i in NormDict2:
        NormDict2[i]=NormDict2[i]+dict1[i]
    else:
        NormDict2[i]=dict1[i]
print(NormDict2)
