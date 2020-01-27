import pygame
import os
import sys
from ressources.Character import Character
from ressources.Characteristics import Characteristics
from ressources.Entity import Entity
from ressources.Inventory import Inventory
from ressources.Monster import Monster
from ressources.Potion import Potion
from ressources.Weapon import Weapon


SCRIPTPATH = os.path.realpath(__file__).replace("\\main.py", "")


pygame.init()

# Générer la fenetre du jeu 
pygame.display.set_caption("Zelda Python")
SCREEN = pygame.display.set_mode((1080, 720))  # Le set_mode renvoie une surface

# Importer et charger le background  de notre jeu 
BACKGROUND = pygame.image.load(SCRIPTPATH + '/assets/backgrounds/canyon.jpg')
# Redimensioner le background à la taille de notre screen
BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))

RUNNING = True

PRESSED = {} #Dictionnaire des touches qui sont actuellement enfoncées


CHARACTER = Character("Jason", Characteristics(50, 100, 3, 3, 3), Inventory(20), pygame.image.load(SCRIPTPATH + "\\assets\\characters\\test.png"))

MONSTER = Monster("gringo", Characteristics(1000, 1200, 2, 2, 2), pygame.image.load(SCRIPTPATH + "\\assets\\characters\\test.png"))

# Boucle tant que running = true 
while RUNNING:

    # Appliquer le background à notre fenêtre et gérer l'espacement
    SCREEN.blit(BACKGROUND, (0, 0))  # blit(nomdubackground,(largeur,longueur))

    # Appliquer l'image du joueur et gérer ses déplacement via son attribut __rect
    SCREEN.blit(CHARACTER.getImage(), CHARACTER.getRect())
    
    if PRESSED.get(pygame.K_RIGHT):
        CHARACTER.moveRight()
    elif PRESSED.get(pygame.K_LEFT):
        CHARACTER.moveLeft()
        
    # Mettre à jour l'écran 
    pygame.display.flip()

    # Detecter si le joueur ferme la fenêtre 
    for event in pygame.event.get():
        # Si l'evenement est la fermeture de la fenetre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    # Detecter si le joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            #quelle touche a été utilisée
            PRESSED[event.key] = True
        
        elif event.type == pygame.KEYUP:
            PRESSED[event.key] = False