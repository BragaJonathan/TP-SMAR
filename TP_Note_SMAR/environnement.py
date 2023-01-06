import itertools
import random

from pygame.math import Vector2

import core
from TP_Note_SMAR.agent import Agent
from TP_Note_SMAR.body import Body
from TP_Note_SMAR.fustrum import Fustrum


class Environnement :
    def __init__(self):
        self.hauteur = core.WINDOW_SIZE[0]
        self.longueur = core.WINDOW_SIZE[1]
        # self.listeAgent = []
        # self.listeCreep = []
        # self.listeObstacle = []
        self.objList = []


    # Ajouter une fonction « computePerception » qui calculera la perception de tous les
    # agents et stockera la liste des objets perçus dans une liste du fustrum
    def computePerception(self):
        # objList = list(itertools.chain(self.listeAgent, self.listeCreep, self.listeObstacle))
        # Pour chaque Agent dans listeObj de l'environnement
        for agent in self.objList:
            if isinstance(agent,Agent) :
                # Pour chaque objet dans le champ de vision de l'Agent
                for obj in self.objList:
                    if agent.body.fustrum.inside(obj) :
                        # On l'ajoute dans la liste des perceptions de l'agent
                        agent.listPerception.append(obj)
            agent.listPerception.remove(agent)

    #Ajouter une fonction « compteDecision » qui calculera la décision (mouvement) de tous les agents
    def computeDecision(self):
        for agent in self.objList:
            if isinstance(agent,Agent) :
                agent.update()

    #Ajouter une fonction « applyDecision » qui déplacera les agents
    def applyDecision(self):
        for agent in self.objList:
            if isinstance(agent,Agent) :
                decision = agent.update()
                agent.body.move(decision)

    #Ajouter une fonction « draw » qui affichera les agents et les objets
    def draw(self):
        for obj in self.objList :
            if isinstance(obj,Agent) :
                # color, center, radius
                core.Draw.circle((255, 255, 255), obj.body.position, 10)

    # Ajouter une liste d’agents
    def addAgent(self,agentList):
        self.objList.append(agentList)

    # Ajouter une liste de creeps
    def addCreep(self,creepList):
        self.objList.append(creepList)

    # Ajouter une liste d’agents
    def addObstacle(self,obstacleList):
        self.objList.append(obstacleList)
