import turtle
from turtle import *
import sys
sys.setrecursionlimit(5000)

"""
---------------------------------------------------------------| La v2 de la fonction deepFind, en cours de dev |------------------------------------------------------------
"""

def SearchingDos(dos, file, cycle=0, root='', listRoot =[]):
    if cycle == 0:
        listRoot = []
    """
    :param dos: Le dictionnaire ou la liste entrante
    :param file: Le fichier ou dossier à chercher
    :param cycle: Le nombre de cycle de récursivité, indique la profondeur d'un ficher
    :param root: La racine passante, permet de faire le lien entre le cycle n et n-1
    :return:
    """
    cycle += 1
    if type(dos) == dict:
        for dos_in in dos:
            """
            :param root_in: une racine créé à chaque noeud contenant l'historique du chemin suivit précédemment (root), 
                            auquel on ajoute le dossier actuellement ouvert
            """
            root_in = root + dos_in + "/"

            if str(dos_in) == str(file):
                listRoot.append(root_in)
            SearchingDos(dos[dos_in], file, cycle, root_in, listRoot)

    if type(dos) == list:
        for dos_in in dos:
            if str(dos_in) == str(file):
                listRoot.append(root)

    return file,listRoot

# --------------------------------------------------------------------------------------------------------------------------------------------------------
"""
simWordCoef |Une fonction qui analyse le pourcentage de similarité de deux mots, pour cela on compare le nombre de lettre en commun
"""

def sameWordCoef(word, sameWord):
    """
    :param word: Le mot qu'on cherche
    :param sameWord: Le mot comparé avec le premier
    :return:
    """
    nb = 0
    charCheck = []
    if len(word) < len(sameWord):
        word, sameWord = sameWord, word
    word=word.lower()
    sameWord.lower()

    for char in word:
        if char not in charCheck:
            charCheck.append(char)
            if char in sameWord:
                if word.count(char) <= sameWord.count(char):
                    nb += word.count(char)
                elif word.count(char) > sameWord.count(char):
                    nb += sameWord.count(char)
    return nb / len(word)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

"""
SearshingWord |une fonction qui ressoit un mot et une liste de mots à comparer ,
               sort le ou les mots qui ressemble le plus sous forme de list 
"""


def SearshingWord(ListWords, Word):
    """

    :param ListWords: La liste de mots à comparer
    :param Word: Le mot cherché
    :return:
    """
    coefWord = [["", 0]]
    for word_in in ListWords:
        if sameWordCoef(word_in, Word) > coefWord[0][1]:
            coefWord = [[word_in, sameWordCoef(word_in, Word)]]
        elif sameWordCoef(word_in, Word) == coefWord[0][1]:
            coefWord.append([word_in, sameWordCoef(word_in, Word)])
    words = []
    for word in coefWord:
        words.append(word[0])
    return words

# --------------------------------------------------------------------------------------------------------------------------------------------------------
"""
listingFile | Reçoit un dossier/dictionnaire | Retourne un liste contenant la totalité des fichier dans le répertoire
"""
def listingFile (dos,cycle=0,listingFiling = []):
    if cycle == 0:
        listingFiling =[]

    cycle += 1
    if type(dos) == dict:
        for dos_in in dos:
            listingFile(dos[dos_in], cycle,listingFiling)

    if type(dos) == list:
        for dos_in in dos:
            listingFiling.append(dos_in)

    return listingFiling
# --------------------------------------------------------------------------------------------------------------------------------------------------------
"""
listingDos | Reçoit un dossier/dictionnaire, |Retourne un liste contenant la totalité des dossiers dans le répertoire
"""
def listingDos (dos,cycle=0,listingdosing = []):
    if cycle == 0:
        listingdosing = []
    cycle+=1
    if type(dos)==dict:
        for dos_in in dos:
            listingdosing.append(dos_in)
            listingDos(dos[dos_in],cycle,listingdosing)

    return listingdosing

# --------------------------------------------------------------------------------------------------------------------------------------------------------
def listingDosFIle (dos):
    return listingDos(dos)+listingFile(dos)
# --------------------------------------------------------------------------------------------------------------------------------------------------------

"""
sameCharGroupe | Reçois deux mots | Retourne les groupes de characters en commun des deux mots
"""
def sameCharGroupe (word1, word2):
    wo1 = ""
    listeWord = []
    wo2 = ""
    Check1 = False
    Check2 = False
    for i in range(len(word1)):
        for ii in range(i,len(word1)):
            wo1 += word1[ii]
            if wo1 in word2.lower() and not (len(wo1)<len(wo2)):

                wo2 = wo1
                Check1 = True
            else:
                Check1 = False
            if not Check1 and Check2:
                if len(wo2) > 1:
                    listeWord.append(wo2)

            Check2 = Check1

        wo1=''

    return listeWord,len(listeWord)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
outword |Reçois un mots et une liste de mots | Retourne le mot le plus proche selon lui 
"""
def outword(word, Base):
    ListeDosFile_checked = []
    ListeDosFile= Base
    for name_checked in ListeDosFile:
        if name_checked not in ListeDosFile_checked:
            ListeDosFile_checked.append(name_checked)

    outWord= None
    outCharGroupe = []
    outCharGroupe_check =[]
    check = True
    for dosFile in ListeDosFile_checked:
        if word.lower() == dosFile.lower():
            outWord = [dosFile]
            check = False
        elif check:
            sameWordGroupe = sameCharGroupe(word,dosFile)
            sameWord_in = sameWordCoef(word,dosFile)
            if sameWordGroupe[0]:
                if dosFile not in outCharGroupe_check:
                    if len(sameWordGroupe[0])>1:
                        outCharGroupe.append([dosFile,len(sameWordGroupe[0]),sameWord_in])
                        outCharGroupe_check.append(dosFile)
                    else:
                        for groupe in sameWordGroupe[0]:
                            if len(groupe) > 2 :
                                outCharGroupe.append([dosFile,len(sameWordGroupe[0]),sameWord_in])
                                outCharGroupe_check.append(dosFile)

    word_in_check = ""
    word_in_check_longueur_out=""
    if check:
        for word_in in outCharGroupe_check:

            if len(sameCharGroupe(word,word_in)[0][0]) > len( word_in_check):
                word_in_check = sameCharGroupe(word, word_in)[0][0]
                word_in_check_longueur_out = word_in

        indice_check = 0
        indice_check_word = []
        for word_in2 in outCharGroupe:

            if word_in2[2] > indice_check:
                indice_check_word=[word_in2[0]]
                indice_check = word_in2[2]
            elif word_in2[2] == indice_check:
                indice_check_word.append(word_in2[0])
        indice_check_word = [indice_check_word]
        indice_check_word.append(indice_check)


        if indice_check_word[1] > sameWordCoef(word,word_in_check_longueur_out):
            outWord = indice_check_word[0]
        else:
            outWord = [word_in_check_longueur_out]


    if outWord == ['']:
        outWord = []
        for name in ListeDosFile_checked:
            if word in name:
                outWord.append(name)
        outWord = [outWord]
        outWord.append(False)
        if not outWord[0] :

            outWord = [['WORD NOT FOUND'],True]
    else:
        outWord = [outWord]
        outWord.append(True)

    return outWord


# --------------------------------------------------------------------------------------------------------------------------------------------------------
"""SearchInBase |Reçois un dictionnaire et une liste des sous dictionnaire ainsi que des mots que contient le 
                 dictionnaire principale | Affiche les roots d'accès au dossier appelé dans l'interface
              
"""
def SearchInBase (dos,DataBase):
    word = ''
    while 'stop_run' not in word.lower():
        word = input('\n |-------------------------------------------------------------'
                     '\n Entrée |Stop_run| pour arrêter \n \n Que chercher vous ? : ')
        if 'stop_run' not in word.lower():
            Input = outword(word, DataBase)

            for name in Input[0]:
                if name != 'WORD NOT FOUND':
                    print(SearchingDos(dos, name))

                else:
                    print('WORD NOT FOUND')

            if Input[1] == False:
                print('ATTENTION, Recherche imprecise')

def drawDos (dos, dist=100, alpha=120, cycle=0, cl='black'):

    speed(1200)
    if cycle == 0:
        dot(20, 'black')
        angle  = 360/(len(dos))
        colors =['cyan','#ff00b7','#00d924','#ff5900','#ff38ca','#9e07f0','#288bed','#00ffff']
        nb = 0
        for dos_in in dos :
            color(colors[nb])

            forward(dist)
            write(dos_in)

            drawDos(dos[dos_in], dist - 5 * cycle, alpha, cycle+1, colors[nb])
            nb += 1
            backward(dist)
            right(angle)

    else:
        if type(dos)== list:
            if len(dos) >1:
                left(alpha/2)
                angle = alpha/(len(dos)-1)
                nbi = 0
                for dos_in in dos:
                    forward(dist)
                    right(alpha/2 - nbi * angle)
                    forward(dist)
                    write(dos_in)
                    backward(dist)
                    left(alpha/2 - nbi * angle)
                    nbi += 1
                    backward(dist)
                    right(angle)
                left(alpha/2+angle)

            else:
                for dos_in in dos :
                    forward(dist)
                    write(dos_in)
                    backward(dist)

        elif type(dos) == dict:
            if len(dos)>1:
                left (alpha/2)
                angle = alpha/(len(dos)-1)
                nbi = 0
                for dos_in in dos:
                    forward(dist)
                    right(alpha/2-nbi*angle)
                    forward(dist)
                    dot(10,cl)
                    txt = dos_in + ','+str(cycle)
                    write(txt)


                    drawDos(dos[dos_in], dist - 5 * cycle+1, alpha, cycle+1, cl)
                    backward(dist)
                    left(alpha/2-nbi*angle)
                    nbi += 1
                    backward(dist)
                    right(angle)

                left(alpha/2+angle)

            else:

                for dos_in in dos:
                    forward(dist)
                    txt = dos_in+','+str(cycle)
                    write(txt)

                    drawDos(dos[dos_in], dist - 5 * cycle, alpha, cycle+1, cl)
                    backward(dist)
