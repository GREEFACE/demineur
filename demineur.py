#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
from random import randint
 
if __name__ == '__main__':
    plateau = []
    longueur = 4
    r = 0
    for i in range(longueur):          
        plateau.append([0] * longueur)
 
   
    for i in range(longueur):
        for j in range(longueur):
            r = randint(1, longueur)
 
            if r == longueur:
                plateau[i][j] = "B"
 
    
    for i in range(longueur):
        for j in range(longueur):
            nbBombes = 0
            if plateau[i][j] != "B":
                if j > 0: 
                    if plateau[i][j-1] == "B":
                        nbBombes += 1
                if j < longueur-1:
                    if plateau[i][j+1] == "B":
                        nbBombes += 1
                if i > 0: 
                    #
                    if j > 0: #haut gauche
                        if plateau[i-1][j-1] == "B":
                            nbBombes += 1
                    #haut
                    if plateau[i-1][j] == "B":
                        nbBombes += 1
                    if j < longueur-1: #haut droite
                        if plateau[i-1][j+1] == "B":
                            nbBombes += 1
                if i < longueur-1: #si on est pas dernière ligne
                    if j > 0: #bas gauche
                        if plateau[i+1][j-1] == "B":
                            nbBombes += 1
                    #bas
                    if plateau[i+1][j] == "B":
                        nbBombes += 1
                    if j < longueur-1: #bas droite
                        if plateau[i+1][j+1] == "B":
                            nbBombes += 1
                #maj de la case
                plateau[i][j] = nbBombes
#debug
            print ("case " + str(i) + "/" + str(j) + " = " + str(nbBombes))
    print (plateau)
#fin debug

