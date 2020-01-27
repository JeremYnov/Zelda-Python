import pygame

from ressources.Entity import Entity
# superclasse: pygame.sprite.Sprite -> Définit notre classs comme une entité visible du jeu dans pygame.

class Character(pygame.sprite.Sprite, Entity) :
    
    """Classe définissant notre personnage principal"""
    
    def __init__(self, name, characteristics, inventory, image): # Notre méthode constructeur
        
        super().__init__()
        self._Entity__name = name
        self._Entity__characteristics = characteristics
        self.__inventory = inventory
        self.__image = image # pygame.image.load('chemin/nomdelimage')
        self.__rect = self.getImage().get_rect()
        
    def getInventory(self):
        return self.__inventory
    
    def getImage(self):
        return self.__image
    
    def getRect(self):
        return self.__rect
            
    def setInventory(self, value):
        self.__inventory = value
    
    def setImage(self, value):
        self.__image = value
        
    def setRect(self, value):
        self.__rect = value