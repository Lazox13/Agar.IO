###############################################
# Créateur : MARQUEZ, RABHI                   #
# Date : 14/06/2022                           #
# Programme main AGAR.IO                      #
# Traite le prog. et les sous-prog.           #
# Version : V1.0                              #
###############################################
import core
from carte import Carte
from creep import Creep
from ennemi import Ennemi
from joueur import Joueur


def setup():
    # Crée les variables nécessaire au programme
    # Paramètres fenêtre
    core.memory("Carte", Carte())
    core.memory("JeuxEnCours", False)
    core.memory("JoueurMort", False)

    # Variables joueur
    core.memory("J", Joueur())

    # Variables ennemies
    core.memory("TabE", [])

    for e in range(5):
        core.memory("TabE").append(Ennemi())
        core.memory("TabE")[e].Id += e + 2

    # Variables creeps
    core.memory("TabC", [])

    for c in range(200):
        core.memory("TabC").append(Creep())

    # Variables global joueur/ennemis
    core.memory("TabG", [])
    core.memory("TabG").append(core.memory("J"))
    for e in core.memory("TabE"):
        core.memory("TabG").append(e)


def remiseazero():
    # Remet toutes les variables à zéro
    core.memory("Carte").__init__()
    for i in core.memory("TabG"):
        i.__init__()
    for c in core.memory("TabC"):
        c.__init__()
    for e in range(len(core.memory("TabE"))):
        core.memory("TabE")[e].Id += e + 2


def run():
    # RAZ ecran
    core.cleanScreen()
    if core.memory("JeuxEnCours"):

        # Calcul Listes
        tabg = sorted(core.memory("TabG"), key=lambda r: r.Rayon)

        # Commandes Dessiner | Classement score
        core.memory("Carte").dessiner()
        for c in core.memory("TabC"):
            c.dessiner()
        for i in tabg:
            i.dessiner()
            core.memory("Carte").TableauScores = []
            core.memory("Carte").TableauScores.append(core.memory("J").Rayon)

        # Commandes mouvement
        core.memory("J").mouvement(core.getMouseLeftClick())
        core.memory("Carte").mouvement(core.memory("J").JoueurMouvement)
        for c in core.memory("TabC"):
            c.mouvement(core.memory("J").JoueurMouvement)
        for e in core.memory("TabE"):
            e.mouvement(core.memory("J").JoueurMouvement)
            # print("Jpos", core.memory("J").Pos, "EPos", e.Pos)

        # Commandes manger creep
        for i in tabg:
            for c in core.memory("TabC"):
                if i.Pos.distance_to(c.Pos) < i.Rayon - c.Rayon:
                    c.mourir()
                    i.grossir(c.Rayon)

        # Manger creep/joueur/ennemis | Calcul cible
        distcible = []
        for i in tabg:
            for idecalle in tabg:
                if not i.Id == idecalle.Id:
                    distcible.append(i.Pos.distance_to(idecalle.Pos))
                    if min(distcible) == i.Pos.distance_to(idecalle.Pos):
                        i.cible(idecalle, core.memory("TabC"))

                if i.Pos.distance_to(idecalle.Pos) < i.Rayon - idecalle.Rayon:
                    idecalle.mourir()
                    i.grossir(idecalle.Rayon)
                    if idecalle.jmort():
                        core.memory("JeuxEnCours", False)
                        core.memory("JoueurMort", True)

    else:  # not core.memory("JeuxEnCours")
        if core.memory("Carte").menudecision(core.memory("JeuxEnCours"), core.memory("JoueurMort")):
            remiseazero()
            core.memory("JeuxEnCours", True)
            core.memory("JoueurMort", False)


core.main(setup, run)
