import pygame
from roue import Roue


class Vehicule:

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        self._roue_avant = Roue()
        self._roue_arriere = Roue()
        self._espacement_roues = 60
        self.position = 250

    # ------------------------------
    # propriétés
    # ------------------------------
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self._positionner_les_roues()

    # ------------------------------
    # méthodes
    # ------------------------------
    def _positionner_les_roues(self):
        self._roue_avant.position = self.position + self._espacement_roues / 2
        self._roue_arriere.position = self.position - self._espacement_roues / 2

    def avancer(self, distance):
        self.position += distance

    def reculer(self, distance):
        self.position -= distance

    def dessiner(self, screen):
        # 1 er paramètre  : surface d'affichage (l'écran)
        # 2 ème paramètre : la couleur
        # 3 ème paramètre : la position (centre du cercle)
        # 4 ème paramètre : le diamètre
        pygame.draw.circle(screen, (0, 0, 255), (self.position, 250), 75)
        self._roue_avant.dessiner(screen)
        self._roue_arriere.dessiner(screen)
