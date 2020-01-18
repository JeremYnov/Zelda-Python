import pygame

# Définit notre classs comme une entité du jeu dans pygame
class Player(pygame.sprite.Sprite,Entity) :
    """Classe définissant notre personnage principal"""
    def __init__(self):
        self.image = pygame.image.load('chemin/nomdelimage')
        self.rect = self.image.get_rect()