"""

deepFind | reçois : un dictionnaire, une liste d'éléments à chercher |retourne : un dictionnaire
        Search est une sous fonction de deepFind, elle procède à la recherche d'un élément dans un dictionnaire
"""

""" 
--------------------------------------| La v1 de la fonction qui présente encore des bug |----------------------------------------------------------------------
"""


def deepFind(Reperatorie, list_to_find):
    def Search(dos, file, list_root=[], root="", key=""):
        if root:
            root += "/"
        if key:
            root += str(key)

        if type(dos) == dict:
            for dos_in in dos:
                if dos_in == file:
                    list_root.append(root)
                Search(dos[dos_in], file, list_root, root, dos_in)

        if type(dos) == list:
            for file_in in dos:
                if file_in == file:
                    list_root.append(root)

        return list_root

    lib_root = {}
    for element in list_to_find:
        ens = []
        if Search(Reperatorie, element, ens):
            lib_root[element] = Search(Reperatorie, element, ens)
        else:

            lib_root[element] = 'ERROR: FILE NOT FOUND'
    return lib_root


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
                #print(root)
                listRoot.append(root_in)
            # print (dos_in,cycle,root_in)
            SearchingDos(dos[dos_in], file, cycle, root_in, listRoot)

    if type(dos) == list:
        for dos_in in dos:
            # print (dos_in,cycle,root)
            if str(dos_in) == str(file):
                #print(root)
                listRoot.append(root)
        # print ("")

    return file,listRoot


# --------------------------------------------------------------------------------------------------------------------------------------------------------
"""
simWordCoef |Une fonction qui analyse le pourcentage de similarité de deux mots
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
                # print(char,'OK')
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
listingFile | Reçoit un dossier/dictionnaire, |Retourne un liste contenant la totalité des fichier dans le répertoire
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
            #print (dos_in,cycle)
            listingFiling.append(dos_in)
        # print ("")

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
            #print (dos_in)
            listingdosing.append(dos_in)
            listingDos(dos[dos_in],cycle,listingdosing)

    return listingdosing

# --------------------------------------------------------------------------------------------------------------------------------------------------------
def listingDosFIle (dos):
    return listingDos(dos)+listingFile(dos)
# --------------------------------------------------------------------------------------------------------------------------------------------------------

"""
sameCharGroupe
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
                #print(wo1,'OK')
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

def outword(word, dos):
    ListeDosFile_checked = []
    ListeDosFile= listingDosFIle(dos)
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
            #print(sameCharGroupe(word, word_in)[0][0],word_in_check,sameCharGroupe(word, word_in)[1])
            if len(sameCharGroupe(word,word_in)[0][0]) > len( word_in_check):
                word_in_check = sameCharGroupe(word, word_in)[0][0]
                word_in_check_longueur_out = word_in

        indice_check = 0
        indice_check_word = []
        for word_in2 in outCharGroupe:
            #print(word_in2[2], indice_check)
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

