from math import inf


class Point:
    #setters
    def setX(self,x):
        self._x=x
    def setY(self,y):
        self._y=y
    def setScore(self,score):
        self._score=score
    def setNeighbors(self,neighbors):
        self._neighbors=neighbors
    #getters
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getScore(self):
        return self._score
    def getNeighbors(self):
        return self._neighbors
    

    def __init__(self,x,y,score):
        self.setX(x)
        self.setY(y)
        self.setScore(score)

    def addNeighbor(self,neighbor):
        ls=self.getNeighbors()
        ls.append(neighbor)
        self.setNeighbors(ls)


    def same_coordinates(self, point2) -> bool:
        
        return self.getX() == point2.getX() and self.getY() == point2.getY()
    
    def getUpNeighbor(self,polices,voleur):
        for neighbor in self.getValidNeighbors(polices,voleur):
            if neighbor.getY()<self.getY() and neighbor.getX()==self.getX():
                return neighbor
        for neighbor in self.getValidNeighbors(polices,voleur):
            if neighbor.getY()<self.getY():
                return neighbor    
        
        return None
    def getDownNeighbor(self,polices,voleur):
        for neighbor in self.getValidNeighbors(polices,voleur) :
            if neighbor.getY()>self.getY() and neighbor.getX()==self.getX():
                return neighbor
        for neighbor in self.getValidNeighbors(polices,voleur):
            if neighbor.getY()>self.getY():
                return neighbor    
        
        return None
    
    def getRightNeighbor(self,polices,voleur):
        for neighbor in self.getValidNeighbors(polices,voleur) :
            if neighbor.getX()>self.getX() and neighbor.getY()==self.getY():
                return neighbor
            
        for neighbor in self.getValidNeighbors(polices,voleur):
            if neighbor.getX()>self.getX():
                return neighbor
        return None
    
    def getLeftNeighbor(self,polices,voleur):
        for neighbor in self.getValidNeighbors(polices,voleur) :
            if neighbor.getX()<self.getX() and neighbor.getY()==self.getY():
                return neighbor
        for neighbor in self.getValidNeighbors(polices,voleur):
            if neighbor.getX()<self.getX():
                return neighbor
        return None
    def valid_move(self,move:int,polices,voleur):
        x, y = self.getX(), self.getY()
        if move == 1:  # Up
            
            return self.getUpNeighbor(polices,voleur)
        elif move == 2:  # Down
            return self.getDownNeighbor(polices,voleur)
        elif move == 3:  # Left
            return self.getLeftNeighbor(polices,voleur)
        elif move == 4:  # Right
            return self.getRightNeighbor(polices,voleur)
        else:
            return None  # Invalid move
        
    def getValidNeighbors(self, polices, voleur):
        valid_neighbors = []
        
        # Parcours de tous les voisins du point
        for neighbor in self.getNeighbors():
            # Vérifie si le voisin ne contient ni de police ni de voleur
            if not any(police.getPoint().same_coordinates(neighbor) for police in polices) and not voleur.getPoint().same_coordinates(neighbor):
                valid_neighbors.append(neighbor)
        
        return valid_neighbors