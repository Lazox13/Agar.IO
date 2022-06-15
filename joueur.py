###############################################
# Créateur : MARQUEZ, RABHI                   #
# Date : 14/06/2022                           #
# Sous-Programme joueur de AGAR.IO            #
# Traite le joueur et ses fonctions           #
# Version : V1.0                              #
###############################################
import pygame
from pygame import Vector2
import core


class Joueur:
    def __init__(self):
        # Init joueur
        self.Pos = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.Couleur = (0, 200, 0)
        self.CouleurExt = (0, 100, 0)
        self.Rayon = 15
        self.RayonMax = 150

        # Init mouvement
        self.JoueurMouvement = Vector2()
        self.Accel = Vector2()
        self.U = Vector2()
        self.Vitesse = Vector2()
        self.l = 0
        self.l0 = 20
        self.Raideur = 0.0001
        self.VitesseMin = 0.2
        self.VitesseMax = 0.01
        self.AccelMax = 0.015

        # Init bordure
        self.P1 = 0 - core.WINDOW_SIZE[0]
        self.P2 = 0 - core.WINDOW_SIZE[1]
        self.P3 = core.WINDOW_SIZE[0] * 2
        self.P4 = core.WINDOW_SIZE[1] * 2
        self.Bordure = Vector2(1, 1)

        # Init Id objet
        self.Id = 1

    def dessiner(self):
        pygame.draw.circle(core.screen, self.CouleurExt, self.Pos, self.Rayon)
        pygame.draw.circle(core.screen, self.Couleur, self.Pos, self.Rayon / 1.25)

    def mouvement(self, clic):
        self.bordure()

        if clic is not None:
            self.l = self.Pos.distance_to(clic)
            self.U = clic - self.Pos
            self.U = self.U.normalize()

            self.Accel = Vector2(self.U * self.Raideur * abs(self.l - self.l0))

        if self.Accel.length() > self.AccelMax and self.Accel.length() != 0:
            self.Accel.normalize()
            self.Accel.scale_to_length(self.VitesseMax)

        self.Vitesse += self.Accel

        if self.Vitesse.length() > self.VitesseMax:
            self.Vitesse.scale_to_length(self.VitesseMax)

        self.JoueurMouvement += self.Vitesse

        self.Accel = Vector2(0, 0)
        self.Vitesse = Vector2(0, 0)

    def grossir(self, rayoncible):
        if self.Rayon < self.RayonMax:
            self.Rayon = self.Rayon + rayoncible / 3

    def bordure(self):
        # Position des bords de la carte
        self.P1 -= self.JoueurMouvement.x
        self.P2 -= self.JoueurMouvement.y
        self.P3 -= self.JoueurMouvement.x
        self.P4 -= self.JoueurMouvement.y

        if self.P2 > core.WINDOW_SIZE[1] / 2:
            self.Bordure.y = 0
            if self.JoueurMouvement.y > 0:
                self.Bordure.y = 1

        if self.P4 < core.WINDOW_SIZE[1] / 2:
            self.Bordure.y = 0
            if self.JoueurMouvement.y < 0:
                self.Bordure.y = 1

        if self.P1 > core.WINDOW_SIZE[0] / 2:
            self.Bordure.x = 0
            if self.JoueurMouvement.x > 0:
                self.Bordure.x = 1

        if self.P3 < core.WINDOW_SIZE[0] / 2:
            self.Bordure.x = 0
            if self.JoueurMouvement.x < 0:
                self.Bordure.x = 1

        self.JoueurMouvement.x = self.JoueurMouvement.x * self.Bordure.x
        self.JoueurMouvement.y = self.JoueurMouvement.y * self.Bordure.y

    def jmort(self):
        return True

    # Utile seulement pour les ennemis
    def mourir(self):
        pass

    def cible(self, a, b):
        pass

    def attaquer(self, a):
        pass

    def fuir(self, a):
        pass

    def mangercreep(self, a, b):
        pass
