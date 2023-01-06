import random

from pygame.math import Vector2

from TP_Note_SMAR.body import Body

import core

class Agent:

    def __init__(self, state):
        self.statut = state
        self.body = Body()
        self.listPerception = []
        self.uuid = random.randint(10000,99999)

    def show(self):
        if self.statut == "S":
            core.Draw.circle((0, 0, 255), self.body.position, self.body.taille)
        elif self.statut == "I":
            core.Draw.circle((255, 0, 0), self.body.position, self.body.taille)
        elif self.statut == "R":
            core.Draw.circle((0, 255, 0), self.body.position, self.body.taille)
        else:
            core.Draw.circle((255, 255, 255), self.body.position, self.body.taille)


    def filtre(self):
        centre = None
        voisins = []
        for p in self.listPerception:
            voisins.append(p)
        return voisins, centre

    def update(self):
        voisin, target = self.filtre()

        repulsion = Vector2(0,0)
        if target is None:
            return Vector2(random.random() * 2 -1, random.random() * 2 -1)
        for v in voisin:
            repulsion += self.body.position - v.position
        if len(voisin) != 0:
            repulsion /= len(voisin)

        attraction = target.position - self.body.position

        return repulsion+attraction