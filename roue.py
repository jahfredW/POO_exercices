import pygame

class Roue:

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        # on initialise les membres privées de la Class
        # en passant par les propriétés de la Class
        self.position = 250
        self.diametre = 25

    # ------------------------------
    # propriétés
    # ------------------------------
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def diametre(self):
        return self._diametre

    @diametre.setter
    def diametre(self, value):
        self._diametre = value

    # ------------------------------
    # méthodes
    # ------------------------------
    def dessiner(self, screen):
        # 1 er paramètre  : surface d'affichage (l'écran)
        # 2 ème paramètre : la couleur
        # 3 ème paramètre : la position (centre du cercle)
        # 4 ème paramètre : le diamètre
        pygame.draw.circle(screen, (50, 50, 255), (self.position, 320), self.diametre)
