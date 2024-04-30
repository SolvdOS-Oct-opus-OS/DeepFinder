from tools import *
import json5

with open('Repertoir.json5', encoding='UTF-8') as lib:
    dico = json5.load(lib)




liste = ['Thermo','ElectroStat','MagnétoStat','ssfdQDddDdqd.PNG',
         'Italie.jpg','MontBlancKeket.gif','Tetrice',
         'Horloge','link_with_windows']

print(SershingDos(dico,'link_with_windows'))
print(SearshingWord(liste,"MontBlanc"))
