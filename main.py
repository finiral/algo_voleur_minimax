import tkinter as tk
from tkinter import messagebox
from entity.terrain import Terrain
from interfaceJeu.fenetre import Fenetre
def main():
#initialisation données
    #initialisation des points
    ls_pt=[]
    ls_pt.append(Point(0,0,4))
    ls_pt.append(Point(1,0,3))
    ls_pt.append(Point(-1,0,3))
    ls_pt.append(Point(0,1,3))
    ls_pt.append(Point(0,-1,3))
    ls_pt.append(Point(2,0,2))
    ls_pt.append(Point(-2,0,2))
    ls_pt.append(Point(0,2,2))
    ls_pt.append(Point(0,-2,2))
    ls_pt.append(Point(3,0,1))
    ls_pt.append(Point(-3,0,1))
    ls_pt.append(Point(0,3,1))
    ls_pt.append(Point(0,-3,1))
    ls_pt.append(Point(3,1,1))
    ls_pt.append(Point(3,-1,1))
    ls_pt.append(Point(-3,-1,1))
    ls_pt.append(Point(-3,1,1))
    ls_pt.append(Point(1,3,1))
    ls_pt.append(Point(-1,3,1))
    ls_pt.append(Point(1,-3,1))
    ls_pt.append(Point(-1,-3,1))
    #initialisation des voisins
    for pt in ls_pt:
        neighbors = []
        for other_pt in ls_pt:
            # Vérifie si les coordonnées du point voisin diffèrent d'exactement 1 ou -1 dans l'une des dimensions (x ou y)
            if abs(pt.getX() - other_pt.getX()) == 1 and abs(pt.getY() - other_pt.getY()) <= 1 and pt != other_pt:
                neighbors.append(other_pt)
            elif abs(pt.getY() - other_pt.getY()) == 1 and abs(pt.getX() - other_pt.getX()) <= 1 and pt != other_pt:
                neighbors.append(other_pt)
        pt.setNeighbors(neighbors)

    #Cas SPECIAL 
    ls_pt[13].addNeighbor(ls_pt[17])
    ls_pt[17].addNeighbor(ls_pt[13])

    ls_pt[14].addNeighbor(ls_pt[19])
    ls_pt[19].addNeighbor(ls_pt[14])

    ls_pt[15].addNeighbor(ls_pt[20])
    ls_pt[20].addNeighbor(ls_pt[15])

    ls_pt[16].addNeighbor(ls_pt[18])
    ls_pt[18].addNeighbor(ls_pt[16])
        
    
    # Affichage des voisins pour chaque point
    for pt in ls_pt:
        print("Point ({}, {}), Score: {}".format(pt.getX(), pt.getY(), pt.getScore()))
        print("Neighbors:")
        for neighbor in pt.getNeighbors():
            print("  ({}, {})".format(neighbor.getX(), neighbor.getY()))
        print()

    #initialisation voleur
    vol=Pion(0,0,ls_pt[0],True)
    #initialisation police
    ls_police=[]
    ls_police.append(Pion(1,0,ls_pt[1],False))
    ls_police.append(Pion(-1,0,ls_pt[2],False))
    ls_police.append(Pion(0,-1,ls_pt[4],False))
    #initialisation terrain
    terrain = Terrain(ls_pt, True, vol,ls_police)
    fenetre = Fenetre(terrain)
    fenetre.window.mainloop()


if __name__ == "__main__":
    from entity.pion import Pion
    from entity.point import Point
    main()
