from entity.point import Point


class Pion():
    #setters
    def setX(self,x):
        self._x=x
    def setY(self,y):
        self._y=y
    def setPoint(self,point:Point):
        self._point=point
    def setIsVoleur(self,vol:bool):
        self._isVoleur=vol
    #getters
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getPoint(self):
        return self._point
    def getIsVoleur(self):
        return self._isVoleur
    

    def __init__(self,x,y,point:Point,isVoleur:bool):
        self.setX(x)
        self.setY(y)
        self.setPoint(point)
        self.setIsVoleur(isVoleur)

    def move(self,point:Point):
        self.setX(point.getX())
        self.setY(point.getY())
        self.setPoint(point)
