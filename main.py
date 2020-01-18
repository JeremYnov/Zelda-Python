import pygame

pygame.init()

# Générer la fenetre du jeu 
pygame.display.set_caption("Zelda Python")
screen = pygame.display.set_mode((1080, 720))  # Le set_mode renvoie une surface

# Importer et charger le background  de notre jeu 
background = pygame.image.load('assets/backgrounds/canyon.jpg')
# Redimensioner le background à la taille de notre screen
background = pygame.transform.scale(background, (1280, 720))

running = True

# Boucle tant que running = true 
while running:

    # Appliquer le background à notre fenêtre et gérer l'espacement
    screen.blit(background, (0, 0))  # blit(nomdubackground,(largeur,longueur))

    # Mettre à jour l'écran 
    pygame.display.flip()

    # Si le joueur ferme la fenêtre 
    for event in pygame.event.get():
        # Si l'evenement est la fermeture de la fenetre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
