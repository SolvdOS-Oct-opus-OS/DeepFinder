
"""

deepFind | reçois : un dictionnaire, une liste d'éléments à chercher |retourne : un dictionnaire
        Search est une sous fonction de deepFind, elle procede à la recherche d'un élément dans un dictionnaire
"""



def deepFind (Reperatorie,list_to_find):
    def Search (dos,file,list_root=[],root = "",key = ""):
        if root:
            root+="/"
        if key:
            root += str(key)

        if type(dos) == dict:
            for dos_in in dos:
                if dos_in == file:
                    list_root.append(root)
                Search(dos[dos_in],file,list_root,root,dos_in)

        if type(dos) == list:
            for file_in in dos :
                if file_in == file:
                    list_root.append(root)


        return list_root

    lib_root = {}
    for element in list_to_find:
        ens = []
        if Search(Reperatorie,element,ens):
            lib_root[element] = Search(Reperatorie,element,ens)
        else:

            lib_root[element] = 'ERROR: FILE NOT FOUND'
    return lib_root
