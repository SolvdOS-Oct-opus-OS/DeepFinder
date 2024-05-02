from tools import *
import json5

with open('Repertoir.json5', encoding='UTF-8') as lib:
    dico = json5.load(lib)

word = ''
while 'stop_run' not in word.lower():
    word = input('\n |-------------------------------------------------------------'
                 '\n Entrée |Stop_run| pour arrêter \n \n Que chercher vous ? : ')
    if 'stop_run' not in word.lower():
        Input = outword(word, dico)

        for name in Input[0]:
            if name != 'WORD NOT FOUND':
                print(SearchingDos(dico, name))

            else:
                print('WORD NOT FOUND')

        if Input[1] == False:
            print('ATTENTION, Recherche imprecise')
