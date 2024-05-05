import turtle
from turtle import *
import sys
sys.setrecursionlimit(5000)

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




def drawDos2 (dos, dist=100, alpha=120, cycle=0, cl='black'):

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

            drawDos2(dos[dos_in], dist - 5 * cycle, alpha, cycle+1, colors[nb])
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


                    drawDos2(dos[dos_in], dist - 5 * cycle+1, alpha, cycle+1, cl)
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

                    drawDos2(dos[dos_in], dist - 5 * cycle, alpha, cycle+1, cl)
                    backward(dist)
