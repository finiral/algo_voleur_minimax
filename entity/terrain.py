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
        voleur_point = self.getVoleur().getPoint()
        voleur_score = voleur_point.getScore()
        
        # Calcule la somme des distances entre chaque police et le voleur
        total_distance = sum(sqrt((police.getPoint().getX() - voleur_point.getX() )**2 + ( police.getPoint().getY()- voleur_point.getY() )**2) for police in self.getPolices())
        
        # Plus la somme des distances est petite, plus elle contribue positivement au score
        score_contribution = (1 / total_distance) if total_distance != 0 else float('inf') 

        return score_contribution-voleur_score
    
    def nextMove(self):
        ls_terrain=[]
        if not self._isVoleurTurn:
            pt=self.getVoleur().getPoint()
            voisins=pt.getValidNeighbors(self.getPolices(),self.getVoleur())
            for voisin in voisins:
                new_voleur=Pion(-1,-1,voisin,True)
                new_voleur.move(voisin)
                ls_terrain.append(Terrain(self.getLsPoints(),True,new_voleur,self.getPolices()))
            
        else :
            for police in self.getPolices():
                new_ls=self.getPolices().copy()
                new_ls.remove(police)
                pt=police.getPoint()
                voisins=pt.getValidNeighbors(self.getPolices(),self.getVoleur())

                for voisin in voisins:
                    new_police=Pion(-1,-1,voisin,False)
                    new_police.move(voisin)
                    new_ls.append(new_police)
                    ls_terrain.append(Terrain(self.getLsPoints(),False,self.getVoleur(),new_ls.copy()))
                    new_ls.pop()
        return ls_terrain
    
    def isTerminal(self):
        if len(self.getVoleur().getPoint().getValidNeighbors(self.getPolices(),self.getVoleur()))==0:
            return True
        if self.getVoleur().getPoint().same_coordinates(Point(0,0,99)):
            return True
        return False
    

    