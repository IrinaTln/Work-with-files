trans_word=""
new_word=""
new_word_correction=""

from random import*

def read_from_file(file)->list:
    """Read from file and adding in list
    """
    fail=open(file,'r')
    mas=[] 
    for line in fail:
        mas.append(line.strip())
    fail.close()
    return mas

def new_word(file:str, x:str) ->list:
    """Appending new words in list
    """
    mas=[]
    with open(file,'a') as t:
        t.write("\n"+x)
    mas=read_from_file(file)
    return mas

#def find_in_list_by_word(list_word:list, word:str)->int:
#    return(list_word.index(word))

#def get_word_by_index(list_word:list, index:int):
#    return(list_word[index])

def translate_word(word:str, language:str):
    list_translator=[]
    list_language=[]

    if language=="1":
        list_language=read_from_file("rus.txt")
        list_translator=read_from_file("eng.txt")
    elif language=="2":
        list_language=read_from_file("eng.txt")
        list_translator=read_from_file("rus.txt")

    if word in list_language:
        index_word=list_language.index(word)
        return(list_translator[index_word])
    return()

def study(trans_word:str):
    
    general_list=[]

    rus_list=read_from_file("rus.txt")
    eng_list=read_from_file("eng.txt")

    general_list=rus_list+eng_list

    latin_letters="abcdefghijklmnopqrstuvwxyz"
    cyrillic_letters="абвгдеёжзийклмнопрстуфхцчщщъэюя"

    itterable=0

    while itterable<5:
        itterable+=1

        word=(choice(general_list))
        print("Слово для перевода: ", word)
        trans_word=input("Ваш перевод: ")

        for i in word:
            if i in cyrillic_letters:
                index=rus_list.index(word)
            elif i in latin_letters:
                index=eng_list.index(word)
        
        for k in trans_word:
            if k in cyrillic_letters:
                index2=rus_list.index(trans_word)
            elif k in latin_letters:
                index2=eng_list.index(trans_word)
       
        if index==index2:
            print("Поздравляем! Ваш перевод верный!")
        else:
            print("Неверный перевод. Попробуйте еще раз!")

    return()

def correction(word:str, mas:list)->list:
    """Correction of errors in list.
        correct a:str
    """
    new_word=input("Введите новое слово: ")
    for i in range (len(mas)):
        if mas[i]==word:
            new_word_correction=word.replace(word, new_word)
            mas.insert(i, new_word_correction)
            mas.remove(word)
            
    return mas

def to_file(mas:list, file:str):

    with open (file, 'w') as f:
        for i in mas:
            f.write(i+"\n")
   

from gtts import gTTS
#from playsound import playsound
import os

def sound(text:str, language:str):
    #language='en', 'fi', 'ru'
    obj=gTTS(text=text, lang=language, slow=False).save("sound.mp3")
    #playsound("sound.mp3")
    os.system("sound.mp3")


#import pyttsx3

#def sound2(text_str, language):
#    sound==pyttsx3.init()
#    sound.setProperty('volume',0.5)
#    sound.setProperty('rate', 150)#>100
#    #sound.setProperty('voice')
#    sound.say(text)
#    sound.runAnWait()
