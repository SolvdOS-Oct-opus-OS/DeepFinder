import turtle
from turtle import *
import sys
sys.setrecursionlimit(5000)
from tools import *
from DevZone import *
import json5
from random import *



with open('Repertoir.json5', encoding='UTF-8') as lib:
    dico = json5.load(lib)
    DataBase = listingDosFIle(dico)
    #SearchInBase(dico,DataBase)
    lib.close()


print(SearchingDos(dico,'Driver'))


turtle.bgcolor('black')
drawDos(dico, 80, 120)
mainloop()


with open ('ColorsBase.json5',encoding='UTF-8') as ColorsFile:
    Colors = json5.load(ColorsFile)
    ColorsFile.close()
colorListeUsed = []
colorListe = []
for color in Colors['Neon']:
    colorListe.append(color)

for i in range (100):
    clr = colorListe[randint(0,len(colorListe)-1)]
    if clr not in colorListeUsed:
        colorListeUsed.append(clr)
        print (clr)
