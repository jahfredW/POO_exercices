import pygame
from vehicule import Vehicule
from voiture import Voiture

# imports nécessaires pour la détection des touches clavier (interaction utilisateur)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

if __name__ == '__main__':

    voiture1 = Vehicule('blue')

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # configuration initiale de la librairie pygame
    pygame.init()

    # configuration de l'écran d'affichage
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Lancement de la boucle de jeu
    running = True
    while running:

        # Détection des entrées utilisateur
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Si on appuie sur le bouton ECHAP, on arrête le programme
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_RIGHT:
                    voiture1.avancer(10)
                    #voiture2.avancer(10)
                if event.key == K_LEFT:
                    voiture1.reculer(10)
                    #voiture2.reculer(10)
            if event.type == pygame.QUIT:
                running = False

        # on affiche un fond blanc
        screen.fill((255, 255, 255))

        # on dessine le ou les véhicules
        voiture1.dessiner(screen)

        # mise à jour de l'affichage
        pygame.display.flip()

    # On sert du programme, on libère les ressources utilisées
    pygame.quit()
