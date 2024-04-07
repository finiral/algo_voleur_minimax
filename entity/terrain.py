from math import sqrt
from entity.pion import Pion
from entity.point import Point
from typing import List
class Terrain:

    """ SETTERS """
    def setLsPoints(self,ls):
        self._lsPoints=ls
    def setIsVoleurTurn(self,turn:bool):
        self._isVoleurTurn=turn
    def setVoleur(self,pt:Pion):
        self._voleur=pt
    def setPolices(self,pt):
        self._polices=pt

    
    """ GETTERS """
    def getLsPoints(self):
        return self._lsPoints
    def getIsVoleurTurn(self):
        return self._isVoleurTurn
    def getVoleur(self):
        return self._voleur
    def getPolices(self):
        return self._polices
    
    
    def __init__(self,lspoints,isvoleurturn:bool,voleur:Pion,police):
        self.setLsPoints(lspoints)
        self.setIsVoleurTurn(isvoleurturn)
        self.setVoleur(voleur)
        self.setPolices(police)
    

    def getEvaluation(self):
        if self.isVoleurWin():
            return float("inf")
        elif self.isPoliceWin():
            return float("-inf")
        else:
            voleur_point = self.getVoleur().getPoint()
            
            # Calcule la distance entre le voleur et le point (0, 0)
            distance_to_center = (sqrt(voleur_point.getX()**2 + voleur_point.getY()**2))
            
           
            # Calcule la somme des distances entre chaque policier et le voleur
            sum_distance=0
            for police in self.getPolices():
                sum_distance+=sqrt((police.getPoint().getX() - voleur_point.getX())**2 + (police.getPoint().getY() - voleur_point.getY())**2)

            
            # Soustrait le nombre de mouvements valides du voleur
            moves = len(self.getVoleur().getPoint().getValidNeighbors(self.getPolices(), self.getVoleur()))

            return moves+sum_distance-distance_to_center
        
    def nextMove(self):
        ls_terrain=[]
        if not self.getIsVoleurTurn():
            pt=self.getVoleur().getPoint()
            voisins=pt.getValidNeighbors(self.getPolices(),self.getVoleur())
            for voisin in voisins:
                new_voleur=Pion(voisin.getX(),voisin.getY(),voisin,True)
                ls_terrain.append(Terrain(self.getLsPoints(),True,new_voleur,self.getPolices()))
            
        else :
            for police in self.getPolices():
                new_ls=self.getPolices().copy()
                new_ls.remove(police)
                pt=police.getPoint()
                voisins=pt.getValidNeighbors(self.getPolices(),self.getVoleur())

                for voisin in voisins:
                    new_police=Pion(voisin.getX(),voisin.getY(),voisin,False)
                    new_ls.append(new_police)
                    ls_terrain.append(Terrain(self.getLsPoints(),False,self.getVoleur(),new_ls.copy()))
                    new_ls.pop()
        return ls_terrain
    

    
    def isVoleurWin(self):
        if self.getVoleur().getPoint().same_coordinates(Point(0,0,99)):
            return True
        return False
    

    def isPoliceWin(self):
        if len(self.getVoleur().getPoint().getValidNeighbors(self.getPolices(),self.getVoleur()))==0:
            return True
        return False
    
    def isTerminal(self):
        if self.isVoleurWin() or self.isPoliceWin():
            return True
        return False
    
    def printTerrain(self):
        print("Coordinates of the police:")
        for police in self.getPolices():
            print(f"Police: ({police.getPoint().getX()}, {police.getPoint().getY()})")
        print(f"Thief: ({self.getVoleur().getPoint().getX()}, {self.getVoleur().getPoint().getY()})")
        print(f"Evaluation of the current terrain: {self.getEvaluation()}")
        print(f"It's {'the thief' if self.getIsVoleurTurn() else 'police'}'s turn.")
        print("\n \n")
        

    