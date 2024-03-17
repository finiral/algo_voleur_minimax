from tkinter import Tk, Canvas

from entity.voleur import Voleur
from interfaceJeu.customcanvas import CustomCanvas


class InterfaceJeu:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Jeu")
        # placer au milieu
        screen_width = self.fenetre.winfo_screenwidth()
        screen_height = self.fenetre.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 600) // 2
        self.fenetre.geometry('{}x{}+{}+{}'.format(500, 600, x, y))

        self.canvasTest = CustomCanvas(self.fenetre, width="600", height="500")

        # placer le terrain au milieu (pixels)
        terrain_x1 = 100 
        terrain_y1 = 130 
        terrain_x2 = 385
        terrain_y2 = 415

        self.terrain = self.canvasTest.create_oval(terrain_x1, terrain_y1, terrain_x2, terrain_y2, outline="black")
        # verticale
        self.ligneVerticale = self.canvasTest.create_line((terrain_x1 + terrain_x2) // 2, terrain_y1, (terrain_x1 + terrain_x2) // 2, terrain_y2, fill="blue")
        # droite horizontale
        self.ligneHorizontale =  self.canvasTest.create_line(terrain_x1, (terrain_y1 + terrain_y2) // 2, terrain_x2, (terrain_y1 + terrain_y2) // 2, fill="green")

        # Calcul du centre du terrain
        centre_x = (terrain_x1 + terrain_x2) // 2
        centre_y = (terrain_y1 + terrain_y2) // 2

        # Coordonnées du cercle au milieu du terrain
        cercle_rayon = 50
        cercle_x1 = centre_x - cercle_rayon
        cercle_y1 = centre_y - cercle_rayon
        cercle_x2 = centre_x + cercle_rayon
        cercle_y2 = centre_y + cercle_rayon

        # Dessiner le cercle au milieu
        self.demiTerrainMilieu = self.canvasTest.create_oval(cercle_x1, cercle_y1, cercle_x2, cercle_y2, outline="black")

        # Dessiner les demi-cercles aux bords du terrain
        rayon_demi_cercle = 50

        # Demi-cercle supérieur
        self.demiCercleSup = self.canvasTest.create_arc(centre_x - rayon_demi_cercle, terrain_y1 - rayon_demi_cercle,
                                    centre_x + rayon_demi_cercle, terrain_y1 + rayon_demi_cercle,
                                    start=180, extent=180, style="arc")

        # Demi-cercle inférieur
        self.demiCercleInf = self.canvasTest.create_arc(centre_x - rayon_demi_cercle, terrain_y2 - rayon_demi_cercle,
                                    centre_x + rayon_demi_cercle, terrain_y2 + rayon_demi_cercle,
                                    start=0, extent=180, style="arc")

        # Demi-cercle gauche
        self.demiCercleGauche = self.canvasTest.create_arc(terrain_x1 - rayon_demi_cercle, centre_y - rayon_demi_cercle,
                                    terrain_x1 + rayon_demi_cercle, centre_y + rayon_demi_cercle,
                                    start=90, extent=-180, style="arc")

        # Demi-cercle droit
        self.demiCercleDroite = self.canvasTest.create_arc(terrain_x2 - rayon_demi_cercle, centre_y - rayon_demi_cercle,
                                    terrain_x2 + rayon_demi_cercle, centre_y + rayon_demi_cercle,
                                    start=-90, extent=-180, style="arc")


        # définition des pions
        self.canvasTest.setVoleur(Voleur(centre_x,centre_y))
        self.canvasTest.draw_voleur()

        


