import pygame
from vehicule import Vehicule
from multipledispatch import dispatch


class Voiture(Vehicule):

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        super().__init__()
        #ajouter ici les initialisations nécessaire à la class enfant Voiture...
        pass

    @dispatch(object)
    def dessiner(self, screen):
        # au lien de dupliquer le code, on utilise celui existant en fournissant la valeur d'une couleur par défaut.
        # Ainsi, le code appelant peut dessiner la voiture sans avoir à sépcifier la couleur, et le code est plus facilement
        # maintenable.
        #
        # Si un bug est identifié dans la méthode édessiner(selfself, screen, color)" il sera corrigé à un seul endroit.

        self.dessiner(screen, (255, 0, 0))

    @dispatch(object, object)
    def dessiner(self, screen, color):
        # 1 er paramètre  : surface d'affichage (l'écran)
        # 2 ème paramètre : la couleur
        # 3 ème paramètre : le rectangle
        pygame.draw.rect(screen, color, pygame.Rect(super().position - 30, 250, 60, 60))
        self._roue_avant.dessiner(screen)
        self._roue_arriere.dessiner(screen)

