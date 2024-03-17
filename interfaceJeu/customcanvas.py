from tkinter import Canvas

from entity.voleur import Voleur


class CustomCanvas(Canvas):
    def __init__(self,fenetre,width,height):
        super().__init__(fenetre,width=width,height=height)
        self.voleur_id=None

    def setVoleur(self,voleur:Voleur):
        self._voleur=voleur

    def getVoleur(self):
        return self._voleur

    def draw_voleur(self):
        if self.voleur_id!=None:
            self.delete(self.voleur_id)
        voleurRayon = 8
        voleur_x1 = self.getVoleur().getX() - voleurRayon
        voleur_y1 = self.getVoleur().getY() - voleurRayon
        voleur_x2 = self.getVoleur().getX() + voleurRayon
        voleur_y2 = self.getVoleur().getY() + voleurRayon
        self.voleur_id=self.create_oval(voleur_x1, voleur_y1, voleur_x2, voleur_y2, fill="green")
        self.pack()
        #Listener
        self.bind_all("<KeyPress>", self.key_pressed)

    def right_voleur(self):
        if self.getVoleur().move_right(47):
            self.draw_voleur()

    def left_voleur(self):
        if self.getVoleur().move_left(47):
            self.draw_voleur()

    def up_voleur(self):
        if self.getVoleur().move_up(47):
            self.draw_voleur()
            
    def down_voleur(self):
        if self.getVoleur().move_down(47):
            self.draw_voleur()

    def key_pressed(self, event):
        if event.keysym == 'Up':
            print("Touche Haut relâchée")
            self.up_voleur()
        elif event.keysym == 'Down':
            print("Touche Bas relâchée")
            self.down_voleur()
        elif event.keysym == 'Left':
            print("Touche Gauche relâchée")
            self.left_voleur()
        elif event.keysym == 'Right':
            print("Touche Droite relâchée")
            self.right_voleur()