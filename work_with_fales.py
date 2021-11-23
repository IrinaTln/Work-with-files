
from module1 import *
from random import *

rus_list=read_from_file("rus.txt")
eng_list=read_from_file("eng.txt")

print(rus_list)
print(eng_list)

words=""
for word in rus_list:
    words=words+" "+ word
sound(words, 'ru')
#a=input()
words=""
for word in eng_list:
    words=words+" "+ word
sound(words, 'en')

while True:

    menu=input("Перевести - tr;\nНовое слово - new;\nОшибка - er;\nКонтроль словарного запаса - cnt;\nКонец работы - l;\n")

    if menu.upper()=="TR":
        v=input("Какой словарь будем использовать:\nРусско-английский - 1\nАнгло-русский - 2?\n")
        translate_word_str=translate_word(input("Введите слово для перевода: "), v)
        if translate_word_str:
            print("Перевод: "+translate_word_str)
        else:
            print("Перевод не найден.")

    elif menu.upper()=="NEW":
        rus_list=new_word("rus.txt", input("Введите новое слово на русском: "))
        eng_list=new_word("eng.txt", input("Insert new word in english: "))
       
    elif menu.upper()=="ER":
        a=input("Какой словарь будем исправлять:\nРусско-английский - 1\nАнгло-русский - 2?\n")
        if a=="1":
            rus_list=correction(input("Введите слово на русском: "), rus_list)
            print(rus_list)
            to_file(rus_list, "rus.txt")
        else:
            eng_list=correction(input("Insert word in english: "), eng_list)
            to_file(eng_list, "eng.txt")
        
    elif menu.upper()=="CNT":
        study=study(trans_word)

    else:
        break

