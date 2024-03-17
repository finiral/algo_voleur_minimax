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
            if(self.up==1):
                self.move_down(increment)
            if(self.down==1):
                self.move_up(increment)
            if(self.up==2):
                self.move_up(increment)
            if(self.down==2):
                self.move_down(increment)
            if(self.up==3 and self.right==1):
                self.setY(self.getY()+increment*2)
                self.setX(self.getX()+increment)
                self.right=2
                self.up=1
                self.left=-2
                self.down=-1
            if(self.down==3 and self.right==1):
                self.setY(self.getY()-increment*2)
                self.setX(self.getX()+increment)
                self.right=2
                self.up=-1
                self.left=-2
                self.down=1
            self.setX(self.getX()+increment)
            self.right+=1
            self.left-=1
            return True
        return False

    def move_left(self,increment):
        if self.left<3:
            if (self.up==1) :
                self.move_down(increment)
            if (self.down==1) :
                self.move_up(increment)
            if(self.up==2):
                self.move_up(increment)
            if(self.down==2):
                self.move_down(increment)
            if(self.up==3 and self.left==1):
                self.setY(self.getY()+increment*2)
                self.setX(self.getX()-increment)
                self.left=2
                self.up=1
                self.right=-2
                self.down=-1
            if (self.down==3 and self.left==1):
                self.setY(self.getY()-increment*2)
                self.setX(self.getX()-increment)
                self.right=-2
                self.up=-1
                self.left=2
                self.down=1
            self.setX(self.getX()-increment)
            self.left+=1
            self.right-=1
            return True
        return False

    def move_up(self,increment):
        if self.up<3:
            if (self.up==0 or self.down==3) and (self.right==1 or self.left==2):
                self.move_left(increment)
            if (self.up==0 or self.down==3) and (self.left==1 or self.right==2):
                self.move_right(increment)
            if (self.up==1 and self.right==3):
                self.setY(self.getY()-increment)
                self.setX(self.getX()-increment*2)
                self.right=1
                self.up=2
                self.left=-1
                self.down=-2
            if (self.up==1 and self.left==3):
                self.setY(self.getY()-increment)
                self.setX(self.getX()+increment*2)
                self.right=-1
                self.up=2
                self.left=1
                self.down=-2
            self.setY(self.getY()-increment)
            self.up+=1
            self.down-=1
            return True
        return False

    def move_down(self,increment):
        if self.down<3:
            if(self.up==0 or self.up==3) and (self.left==1 or self.right==2):
                self.move_right(increment)
            if(self.up==0 or self.up==3) and (self.right==1 or self.left==2):
                self.move_left(increment)
            if(self.right==3 and self.down==1):
                self.setY(self.getY()+increment)
                self.setX(self.getX()-increment*2)
                self.right=1
                self.up=-2
                self.left=-1
                self.down=2
            if(self.left==3 and self.down==1):
                self.setY(self.getY()+increment)
                self.setX(self.getX()+increment*2)
                self.left=1
                self.up=-2
                self.right=-1
                self.down=2
            self.setY(self.getY()+increment)
            self.down+=1
            self.up-=1
            return True
        return False
