# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
dictionary={'a': '?','b': '@','c': '%','d': '*','e': '{','f': ';','g': '+','h': '$','i': '=','j': '&','k': '^','~': '-','m': '`','n': '1','o': '2','p': '3','q': '4','r': '5','s': '6','t': '7','u': '8','v': '9','w': '10','x': '11','y': '12','z': '13'}
word=input("Введите слово на английском языке для перевода:")
normWord=word.lower()
newWord=[]
for i in normWord:
    if i in dictionary:
        i=dictionary[i]
        newWord.append(i)
print(newWord)
Newdictionary={}
for key,value in dictionary.items():
    if value in Newdictionary:
        Newdictionary[value].append(key)
    else:
        Newdictionary[value]=[key]
print(Newdictionary)
anotherWord=input('Напишите сообщение на секртном коде для расшировки обратно')
Obratno=[]
for i in anotherWord:
    if i in Newdictionary:
        i=Newdictionary[i]
        Obratno.append(i)
print(Obratno)



#print('Перевод шифра:', dictionary[normLetter])
