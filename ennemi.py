###############################################
# Créateur : MARQUEZ, RABHI                   #
# Date : 14/06/2022                           #
# Sous-Programme ennemi de AGAR.IO            #
# Traite les ennemis et leurs fonctions       #
# Version : V1.0                              #
###############################################
import core
import random
import pygame
from pygame import Vector2


class Ennemi:
    def __init__(self):
        # Init ennemi
        self.Pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0] * 2),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1] * 2))

        self.Couleur = (255, 0, 0)
        self.Rayon = random.randint(14, 22)
        self.RayonMax = 200

        # Init mouvement
        self.JoueurMouvement = Vector2()
        self.Accel = Vector2()
        self.U = Vector2()
        self.Vitesse = Vector2()
        self.Cible = Vector2()
        self.l = 0
        self.l0 = 50
        self.Raideur = 0.01
        self.VitesseMin = 0.2
        self.VitesseMax = 1
        self.AccelMax = 5

        # Init bordure | zone d'apparition
        self.P1 = 0 - core.WINDOW_SIZE[0]
        self.P2 = 0 - core.WINDOW_SIZE[1]
        self.P3 = core.WINDOW_SIZE[0] * 2
        self.P4 = core.WINDOW_SIZE[1] * 2

        # Init Id objet
        self.Id = 0

    def dessiner(self):
        pygame.draw.circle(core.screen, self.Couleur, self.Pos, self.Rayon)

    def mouvement(self, joueurmouvement):
        self.bordure()
        # Position des bords de la carte
        self.P1 -= joueurmouvement.x
        self.P2 -= joueurmouvement.y
        self.P3 -= joueurmouvement.x
        self.P4 -= joueurmouvement.y

        if self.Cible != self.Pos:
            self.l = self.Pos.distance_to(self.Cible)
            self.U = self.Cible - self.Pos
            self.U = self.U.normalize()

            self.Accel = self.U * self.Raideur * abs(self.l - self.l0)

        if self.Accel.length() > self.AccelMax:
            self.Accel.scale_to_length(self.AccelMax)

        self.Vitesse += self.Accel

        if self.Vitesse.length() > self.VitesseMax:
            self.Vitesse.scale_to_length(self.VitesseMax)

        self.Pos += self.Vitesse - joueurmouvement

    def grossir(self, rayoncible):
        if self.Rayon < self.RayonMax:
            self.Rayon = self.Rayon + rayoncible / 3

    def bordure(self):

        if self.Pos.x < self.P1:
            self.Pos.x = self.P1

        if self.Pos.y < self.P2:
            self.Pos.y = self.P2

        if self.Pos.x > self.P3:
            self.Pos.x = self.P3

        if self.Pos.y > self.P4:
            self.Pos.y = self.P4

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
        self.Rayon = 16
        self.Pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0] * 2),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1] * 2))

        # Contôle nouvelle posisiton
        self.zoneapparition()

        self.Couleur = (255, 0, 0)

    def cible(self, tabg, tabc):
        # Attaque
        if self.Rayon > tabg.Rayon:
            self.attaquer(tabg.Pos)

        # Fuir
        elif self.Rayon < tabg.Rayon and self.Pos.distance_to(tabg.Pos) < 300:
            self.fuir(tabg.Pos)

        # Attaque creep
        else:
            self.mangercreep(tabc)

    def attaquer(self, cible):
        self.Cible = cible

    def fuir(self, cible):
        # Les ennemis sont souvent dirigés vers le coin haut gauche...
        self.Cible = cible * - 1

    def mangercreep(self, tabc):
        distcreep = []
        for creep in tabc:
            calccreep = self.Pos.distance_to(creep.Pos)
            distcreep.append(calccreep)
            if min(distcreep) == calccreep:
                self.Cible = creep.Pos

    # Utile seulement pour joueur
    def jmort(self):
        pass
