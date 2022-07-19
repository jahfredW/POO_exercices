from vehicule import Vehicule
from roue import Roue_camion
import pygame

class Camion(Vehicule):
    def __init__(self, color):
        super().__init__(color)
        self._espacement_roues = 120
        self._roue_avant = Roue_camion()
        self._roue_arriere = Roue_camion()
        self.diametre = 75
        self.position_x = 250
        self.position_y = 450

    def dessiner(self, screen):
        # 1 er paramètre  : surface d'affichage (l'écran)
        # 2 ème paramètre : la couleur
        # 3 ème paramètre : la position (centre du cercle)
        # 4 ème paramètre : le diamètre
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), 75)
        self._roue_avant.dessiner(screen)
        self._roue_arriere.dessiner(screen)
        pygame.draw.rect(screen, self.color, (self.position_x + 10, self.position_y - 90, 100, 100))
