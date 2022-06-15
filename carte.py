###############################################
# Créateur : MARQUEZ, RABHI                   #
# Date : 14/06/2022                           #
# Sous-Programme carte de AGAR.IO             #
# Traite la carte, les menus, le score        #
# Version : V1.0                              #
###############################################
import pygame
import core
from pygame.math import Vector2


class Carte:
    def __init__(self):
        # Init core
        core.WINDOW_SIZE = [800, 800]
        core.bgColor = (255, 255, 255)
        core.fps = 120

        # Init grille
        self.CouleurGrille = (50, 50, 50)
        self.DecalGrille = 100

        self.P1 = 0 - core.WINDOW_SIZE[0]
        self.P2 = 0 - core.WINDOW_SIZE[1]
        self.P3 = core.WINDOW_SIZE[0] * 2
        self.P4 = core.WINDOW_SIZE[1] * 2

        self.PosHautGauche = Vector2(self.P1, self.P2)
        self.PosHautDroite = Vector2(self.P3, self.P2)
        self.PosBasGauche = Vector2(self.P1, self.P4)
        self.PosBasDroite = Vector2(self.P3, self.P4)

        # Init score
        self.TableauScores = []

        # Menu
        self.RetourMenuPrincipal = False

    def dessiner(self):
        self.cadrillage()
        self.bordure()
        # self.tableauscore()

    def bordure(self):
        # Mur Haut
        pygame.draw.line(core.screen, core.bgColor, self.PosHautDroite, self.PosHautGauche, 1)

        # Mur Droite
        pygame.draw.line(core.screen, core.bgColor, self.PosHautDroite, self.PosBasDroite, 1)

        # Mur Bas
        pygame.draw.line(core.screen, core.bgColor, self.PosBasDroite, self.PosBasGauche, 1)

        # Mur Gauche
        pygame.draw.line(core.screen, core.bgColor, self.PosBasGauche, self.PosHautGauche, 1)

    def cadrillage(self):
        for h in range(self.DecalGrille, ((self.P1 * - 1) + self.P3), self.DecalGrille):
            pygame.draw.line(core.screen, self.CouleurGrille,
                             (self.PosHautGauche.x, self.PosHautGauche.y + h),
                             (self.PosHautDroite.x, self.PosHautDroite.y + h), 2)

        for v in range(self.DecalGrille, ((self.P2 * - 1) + self.P4), self.DecalGrille):
            pygame.draw.line(core.screen, self.CouleurGrille,
                             (self.PosHautGauche.x + v, self.PosHautGauche.y),
                             (self.PosBasGauche.x + v, self.PosBasGauche.y), 2)

    def tableauscore(self):
        # Mur Haut
        pygame.draw.line(core.screen, (0, 0, 0), (core.WINDOW_SIZE[0] - 15, 10), (core.WINDOW_SIZE[0] - 250, 10), 1)

        # Mur Droite
        pygame.draw.line(core.screen, (0, 0, 0), (core.WINDOW_SIZE[0] - 50, 50), (core.WINDOW_SIZE[0] - 50, 250), 1)

        # Mur Bas
        pygame.draw.line(core.screen, (0, 0, 0), (core.WINDOW_SIZE[0] - 50, 250), (core.WINDOW_SIZE[0] - 250, 250), 1)

        # Mur Gauche
        pygame.draw.line(core.screen, (0, 0, 0), (core.WINDOW_SIZE[0] - 250, 50), (core.WINDOW_SIZE[0] - 250, 250), 1)

    def mouvement(self, joueurmouvement):
        # Mise à jour des positions avec Mouvement (souris)
        self.PosHautGauche -= joueurmouvement
        self.PosHautDroite -= joueurmouvement
        self.PosBasGauche -= joueurmouvement
        self.PosBasDroite -= joueurmouvement

    def menudecision(self, jeuxencour, mortjoueur):
        core.bgColor = (0, 0, 0)
        if (not jeuxencour and mortjoueur) and not self.RetourMenuPrincipal:
            self.menumort()
            if self.menumort():
                return True

        else:
            self.menuprincipal()
            if self.menuprincipal():
                return True

    def menumort(self):
        core.Draw.text((255, 255, 255), "Perdu", ((core.WINDOW_SIZE[0] / 2) - 50, (core.WINDOW_SIZE[1] / 2) - 200), 50)
        core.Draw.text((255, 255, 255), "Votre score et de" + "" + str(self.TableauScores),
                       ((core.WINDOW_SIZE[0] / 2) - 150, (core.WINDOW_SIZE[1] / 2) - 100), 50)
        core.Draw.text((255, 255, 255), "Appuyez sur r pour rejouer",
                       ((core.WINDOW_SIZE[0] / 2) - 300, (core.WINDOW_SIZE[1] / 2) - 300), 50)
        core.Draw.text((255, 255, 255), "Appuyez sur q pour menu pricipal",
                       ((core.WINDOW_SIZE[0] / 2) - 350, (core.WINDOW_SIZE[1] / 2) - 350), 50)
        if core.getKeyPressList("r"):
            return True
        if core.getKeyPressList("q"):
            self.RetourMenuPrincipal = True

    def menuprincipal(self):
        core.Draw.text((255, 255, 255), "Agar.io", ((core.WINDOW_SIZE[0] / 2) - 50, (core.WINDOW_SIZE[1] / 2) - 200),
                       50)
        core.Draw.text((255, 255, 255), "Appuyez sur espace pour jouer", ((core.WINDOW_SIZE[0] / 2) - 200,
                                                                          (core.WINDOW_SIZE[1] / 2) - 150))
        core.Draw.text((255, 255, 255), "Appuyez sur esc pour quitter", ((core.WINDOW_SIZE[0] / 2) - 400,
                                                                          (core.WINDOW_SIZE[1] / 2) - 400))
        core.Draw.circle((255, 255, 255), ((core.WINDOW_SIZE[0] / 2), (core.WINDOW_SIZE[1] / 2)), 20)
        if core.getKeyPressList("SPACE"):
            return True
        if core.getKeyPressList("ESCAPE"):
            pygame.quit()
