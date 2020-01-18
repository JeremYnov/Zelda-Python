from characteristics import Characteristics

class Entity:
    """Classe définissant une entité (Monstre ou personnage)
    Elle permettra de définir :
    - Son nom 
    - Réccupérer ses caractéristiques
    """
    def __init__(self): # Notre méthode constructeur
        """Constructeur de notre classe"""
        self.name = name
        self.characteristics = Characteristics()