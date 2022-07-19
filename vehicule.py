import matplotlib as matplotlib
import pygame
from roue import Roue

class Vehicule:

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self, color):
        self._color = color
        self._roue_avant = Roue()
        self._roue_arriere = Roue()
        self._espacement_roues = 60
        self.diametre = 75
        self.position_x = 250
        self.position_y = 150


    # ------------------------------
    # propriétés
    # ------------------------------
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        # recuperation du dictionnaire de couleurs
        colorNames = matplotlib.colors.cnames
        # on recupere la clé de la couleur, si elle n'existe pas alors par defaut on met du noir
        self._color = colorNames.get(value)


    @property
    def position_x(self):
        return self._position_x

    @position_x.setter
    def position_x(self, value):
        self._position_x = value
        self._positionner_les_roues_en_x()

    @property
    def position_y(self):
        return self._position_y

    @position_y.setter
    def position_y(self, value):
        self._position_y = value
        self._positionner_les_roues_en_y()

    @property
    def diametre(self):
        return self._diametre

    @diametre.setter
    def diametre(self, value):
        self._diametre = value


    # ------------------------------
    # méthodes
    # ------------------------------
    def _positionner_les_roues_en_x(self):
        print('ici')
        self._roue_avant.position[0] = self.position_x + self._espacement_roues / 2
        self._roue_arriere.position[0] = self.position_x - self._espacement_roues / 2

    def _positionner_les_roues_en_y(self):
        self._roue_avant.position[1] = self.position_y + self.diametre
        self._roue_arriere.position[1] = self.position_y + self.diametre



    def avancer(self, distance):
        self.position_x += distance

    def reculer(self, distance):
        self.position_x -= distance

    def monter(self, distance):
        self.position_y -= distance

    def descendre(self, distance):
        self.position_y += distance

    def dessiner(self, screen):

        # 1 er paramètre  : surface d'affichage (l'écran)
        # 2 ème paramètre : la couleur
        # 3 ème paramètre : la position (centre du cercle)
        # 4 ème paramètre : le diamètre
        try:
            pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), 75)
        except:
            pygame.draw.circle(screen, 'green', (self.position_x, self.position_y), 75)
        self._roue_avant.dessiner(screen)
        self._roue_arriere.dessiner(screen)

