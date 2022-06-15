###############################################
# Créateur : MARQUEZ, RABHI                   #
# Date : 14/06/2022                           #
# Sous-Programme creep de AGAR.IO             #
# Traite les creeps et leurs fonctions        #
# Version : V1.0                              #
###############################################
import core
import random
import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.Pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0] * 2),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1] * 2))
        self.Couleur = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        self.Rayon = 5

        # Init bordure zone d'apparition
        self.P1 = 0 - core.WINDOW_SIZE[0]
        self.P2 = 0 - core.WINDOW_SIZE[1]
        self.P3 = core.WINDOW_SIZE[0] * 2
        self.P4 = core.WINDOW_SIZE[1] * 2

    def dessiner(self):
        pygame.draw.circle(core.screen, self.Couleur, self.Pos, self.Rayon)

    def mouvement(self, joueurmouvement):
        # Mise à jour des positions avec Mouvement (souris)
        self.Pos -= joueurmouvement

        # Position des bords de la carte
        self.P1 -= joueurmouvement.x
        self.P2 -= joueurmouvement.y
        self.P3 -= joueurmouvement.x
        self.P4 -= joueurmouvement.y

    def zoneapparition(self):
        if self.Pos.x < self.P1:
            self.mourir()

        if self.Pos.y < self.P2:
            self.mourir()

        if self.Pos.x > self.P3:
            self.mourir()

        if self.Pos.y > self.P4:
            self.mourir()

    def mourir(self):
        # Remise à zéro des variables
        self.Couleur = core.bgColor
        self.Pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0] * 2),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1] * 2))

        # Contôle nouvelle posisiton
        self.zoneapparition()

        self.Couleur = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
