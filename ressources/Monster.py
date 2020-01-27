import pygame

from ressources.Entity import Entity

class Monster(pygame.sprite.Sprite, Entity):
    
    """Classe définissant les monstres du jeu."""
    
    def __init__(self, name, characteristics, monsterImage): # Notre méthode constructeur
        super().__init__()
        self._Entity__name = name
        self._Entity__characteristics = characteristics
        self.__monsterImage = monsterImage #pygame.image.load('chemin/nomdelimage')
        self.__dropList = [] # __ denotes as a private attribute
    
    def getMonsterImage(self):
        return self.__monsterImage
    
    def getDropList(self):
        return self.__dropList
    
    def setMonsterImage(self, value):
        self.__monsterImage = value
    
    def setDropList(self, value):
        self.__dropList = value