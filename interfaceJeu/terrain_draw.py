from algorithm.ia import IA
from entity.point import Point
from entity.terrain import Terrain
import tkinter as tk


class TerrainDraw(tk.Canvas):

    def setTerrain(self,terrain):
        self.terrain=terrain
    def getTerrain(self):
        return self.terrain
    

    def __init__(self, terrain, **kwargs):
        super().__init__(**kwargs)
        self.terrain=terrain
        self.bind_all("<KeyPress>", self.key_pressed)

    
    
    def draw_terrain(self):
        # Efface le canevas
        self.delete("all")
        
        # Dessine chaque point du terrain
        
        
        # Calcule le décalage pour placer (0, 0) au milieu de la fenêtre
        self.update()
        self.offset_x = self.winfo_width() // 2
        self.offset_y = self.winfo_height() // 2


        for point in self.terrain.getLsPoints():
            x, y = point.getX(), point.getY()
            # Calcule les coordonnées sur le canevas en ajoutant le décalage
            canvas_x = x * 70 + self.offset_x
            canvas_y = y * 70 + self.offset_y
            self.create_rectangle(canvas_x, canvas_y, canvas_x + 10, canvas_y + 10, fill="green")
        
        # Dessine le voleur
        voleur = self.terrain.getVoleur()
        canvas_x = voleur.getX() * 70 + self.offset_x
        canvas_y = voleur.getY() * 70 + self.offset_y
        self.create_oval(canvas_x, canvas_y, canvas_x + 20, canvas_y + 20, fill="red")
        
        # Dessine les polices
        for police in self.terrain.getPolices():
            x, y = police.getX(), police.getY()
            # Calcule les coordonnées sur le canevas en ajoutant le décalage
            canvas_x = x * 70 + self.offset_x
            canvas_y = y * 70 + self.offset_y
            self.create_oval(canvas_x, canvas_y, canvas_x + 20, canvas_y + 20, fill="blue")
        
        
    
    def key_pressed(self, event):
        if self.getTerrain().getIsVoleurTurn():
            x, y = self.getTerrain().getVoleur().getPoint().getX(), self.getTerrain().getVoleur().getPoint().getY()
            move=0
            if event.keysym == 'Up':
                move=1
            elif event.keysym == 'Down':
                move=2
            elif event.keysym == 'Left':
                move=3
            elif event.keysym == 'Right':
                move=4
            
            # Check if the new position is valid and update the voleur's position
            voleur=self.getTerrain().getVoleur()
            polices=self.getTerrain().getPolices()
            if self.getTerrain().getVoleur().getPoint().valid_move(move,polices,voleur) is not None:
                self.getTerrain().getVoleur().move(self.getTerrain().getVoleur().getPoint().valid_move(move,polices,voleur))
                
                self.draw_terrain()  # Redraw the board after the movement
                #tour des polices
                self.launchPoliceTurn()
    
    def launchPoliceTurn(self):
        """ minimax_terrain=IA.minimax(self.getTerrain(),4,True)[2]
        new_terrain=Terrain(self.getTerrain().getLsPoints(),True,self.getTerrain().getVoleur(),minimax_terrain.getPolices())
        self.setTerrain(new_terrain)
        self.draw_terrain() """
        #self.getTerrain().setIsVoleurTurn(True)
        police,move=IA.chooseMove(self.getTerrain().getLsPoints(),self.getTerrain().getPolices(),self.getTerrain().getVoleur())
        for p in self.getTerrain().getPolices():
            if police.getPoint().same_coordinates(p):
                p.move(move)
                break
        self.draw_terrain()