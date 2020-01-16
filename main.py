import pygame 
pygame.init()

# Générer la fenetre du jeu 
pygame.display.set_caption("Zelda Python")
pygame.display.set_mode((1080,720))

running = True

# Boucle tant que running = true 
while running:
    # Si le joueur ferme la fenêtre 
   for event in pygame.event.get():
        # Si l'evenement est la fermeture de la fenetre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()