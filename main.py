from tools import *
import json5

with open('Repertoir.json5', encoding='UTF-8') as lib:
    dico = json5.load(lib)


to_find = ['Fusion','Ba1','Suite_Série']
print (deepFind(dico,to_find))
