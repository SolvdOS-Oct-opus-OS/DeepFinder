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


def SershingDos(dos, file, cycle=0, root='',listRoot =[]):
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
            root_in = root + dos_in + '/'

            if str(dos_in) == str(file):
                #print(root)
                listRoot.append(root_in)
            # print (dos_in,cycle,root_in)
            SershingDos(dos[dos_in], file, cycle, root_in,listRoot)

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


def simWordCoef(word, simWord):
    """
    :param word: Le mot qu'on cherche
    :param simWord: Le mot comparé avec le premier
    :return:
    """
    nb = 0
    charCheck = []
    if len(word) < len(simWord):
        word, simWord = simWord, word
    for char in word:
        if char not in charCheck:
            charCheck.append(char)
            if char in simWord:
                # print(char,'OK')
                if word.count(char) <= simWord.count(char):
                    nb += word.count(char)
                elif word.count(char) > simWord.count(char):
                    nb += simWord.count(char)
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
        if simWordCoef(word_in, Word) > coefWord[0][1]:
            coefWord = [[word_in, simWordCoef(word_in, Word)]]
        elif simWordCoef(word_in, Word) == coefWord[0][1]:
            coefWord.append([word_in, simWordCoef(word_in, Word)])
    words = []
    for word in coefWord:
        words.append(word[0])
    return words
