class Characteristics:
     """Classe définissant les caractéristiques de nos entités (Monstre ou personnage)
    Elle permettra de définir :
    - Les points de vie 
    - Les points de vie maximum
    - Les points d'attaque 
    - Les points de défense 
    - La vitesse 
    """
    def __init__(self):
        self.health = 100
        self.maxHealt = 100
        self.attack = 25
        self.defense = 10
        self.speed = 5