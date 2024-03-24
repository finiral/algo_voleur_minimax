from entity.terrain import Terrain
import tkinter as tk

from interfaceJeu.terrain_draw import TerrainDraw

class Fenetre:
    def __init__(self, terrain:Terrain):
        self.terrain = terrain
        self.window = tk.Tk()
        
        # Calcul de la taille du canevas en fonction du nombre de points
        canvas_width = 800  # Largeur du canevas
        canvas_height = 600  # Hauteur du canevas
        
        # Crée le canevas avec la taille calculée
        self.canvas = TerrainDraw(terrain=self.terrain,master=self.window, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()
        
        # Dessine le terrain lors de l'initialisation
        self.canvas.draw_terrain()