import pygame
from vehicule import Vehicule
from camion import Camion

VITESSE_VEHICULE = 15
VITESSE_CAMION = 10

# imports nécessaires pour la détection des touches clavier (interaction utilisateur)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_z,
    K_a,
    K_o,
    K_p,
    QUIT,
)

if __name__ == '__main__':

    vehicule = Vehicule('yellow')
    camion = Camion('green')

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
                if event.key == K_UP:
                    vehicule.monter(10)
                if event.key == K_DOWN:
                    vehicule.descendre(10)
                if event.key == K_z:
                    vehicule.avancer(VITESSE_VEHICULE)
                if event.key == K_a:
                    vehicule.reculer(VITESSE_VEHICULE)
                if event.key == K_p:
                    camion.avancer(VITESSE_CAMION)
                if event.key == K_o:
                    camion.reculer(VITESSE_CAMION)
            if event.type == pygame.QUIT:
                running = False

        # on affiche un fond blanc
        screen.fill((255, 255, 255))

        # on dessine le ou les véhicules
        vehicule.dessiner(screen)
        camion.dessiner(screen)

        # mise à jour de l'affichage
        pygame.display.flip()

    # On sert du programme, on libère les ressources utilisées
    pygame.quit()