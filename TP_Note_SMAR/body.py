import random

import pygame
from pygame.math import Vector2

import core
from TP_Note_SMAR.fustrum import Fustrum
from TP_Note_SMAR.epidemie import Epidemie

class Body :

    def __init__(self):
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]), random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.acceleration = Vector2()
        self.taille = 10
        self.accMax = 2
        self.vMax = 2
        self.fustrum = Fustrum()
        self.fustrum.parent = self
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.timer = 0
        self.timeInfecte = 0
        self.contagion = False

    def move(self, decision):
        if decision.length()>self.accMax:
            decision.scale_to_length(self.accMax)

        self.vitesse += decision
        if self.vitesse.length()>self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position += self.vitesse

    # fonction update prenant en compte les facteurs de l'épidémie
    def update(self, agent):
        # On incrémente le pas de temps pour l'agent
        self.timer+=1

        # Si l'agent est infecté
        if agent.status == "I":
            # On incrémente son timer d'infection
            self.timeInfecte+=1

            #Si son timer d'infection est supérieur à la durée d'incubation, alors l'agent est contagieux
            if self.timeInfecte > Epidemie().epidemie.get("dureeIncubations"):
                self.contagion = True

            # Si le timer d'infection est supérieur à la durée de décès
            if self.timeInfecte > Epidemie().epidemie.get("dureeDeces"):
                # Alors l'agent a une chance de mourir
                chance = random.randint(0,100)
                if Epidemie().epidemie.get("pourcentageMortalite") < chance/100:
                    agent.status = "M"

            # Si l'agent est infecté et qu'il n'est pas mort, il a une chance de guérir
