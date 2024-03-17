class Pion:
    #setters
    def setX(self,x):
        self._x=x
    def setY(self,y):
        self._y=y
    #getters
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    #constructor
    def __init__(self,x,y):
        self.setX(x)
        self.setY(y)
        self.right=0
        self.left=0
        self.up=0
        self.down=0

    #methods 
    def move_right(self,increment):
        if self.right<3:
            self.setX(self.getX()+increment)
            self.right+=1
            self.left-=1
            return True
        return False

    def move_left(self,increment):
        if self.left<3:
            self.setX(self.getX()-increment)
            self.left+=1
            self.right-=1
            return True
        return False

    def move_up(self,increment):
        if self.up<3:
            self.setY(self.getY()-increment)
            self.up+=1
            self.down-=1
            return True
        return False

    def move_down(self,increment):
        if self.down<3:
            self.setY(self.getY()+increment)
            self.down+=1
            self.up-=1
            return True
        return False
