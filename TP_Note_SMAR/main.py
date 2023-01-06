import itertools
import random

import environnement

from pygame.math import Vector2


from TP_Note_SMAR.agent import Agent

import core

from TP_Note_SMAR.body import Body
from TP_Note_SMAR.epidemie import Epidemie
from TP_Note_SMAR.fustrum import Fustrum


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("agents", [])
    core.memory("item", [])

    for i in range(0, 100):
        core.memory("agents").append(Agent("S"))
    for i in range(0, 1):
        core.memory("agents").append(Agent("I"))


    print("Setup END-----------")

def computePerception(agent):
    objList = core.memory("agents")
    for obj in objList:
        if agent.body.fustrum.inside(obj):
            agent.listPerception.append(obj)

def computeDecision(agent):
    return agent.update()


def applyDecision(agent):
    decision = computeDecision(agent)
    agent.body.move(decision)

def run():
    core.cleanScreen()
     # Display
    for agent in core.memory("agents"):
        agent.show()

    for agent in core.memory("agents"):
         computePerception(agent)

    for agent in core.memory("agents"):
         computeDecision(agent)

    for agent in core.memory("agents"):
         applyDecision(agent)

    for agent in core.memory("agents"):
        if agent.body.position.x <= 0:
            agent.body.vitesse.x *= -1
            agent.body.acceleration *= -1
        elif agent.body.position.x >= 800:
            agent.body.vitesse.x *= -1
            agent.body.acceleration *= -1
        if agent.body.position.y <= 0:
            agent.body.vitesse.y *= -1
            agent.body.acceleration *= -1
        elif agent.body.position.y >= 600:
            agent.body.vitesse.y *= -1
            agent.body.acceleration *= -1

        agent.body.position += agent.body.vitesse

core.main(setup, run)
