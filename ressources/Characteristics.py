class Characteristics:
    
    """Classe définissant les caractéristiques de nos entités (Monstre ou personnage)
    Elle permettra de définir :
    - Les points de vie 
    - Les points de vie maximum
    - Les points d'attaque 
    - Les points de défense 
    - La vitesse 
    """
    def __init__(self, health, maxHealth, attack, defense, speed): # Notre méthode constructeur
        self.__health = health # __ denotes as a private attribute
        self.__maxHealth = maxHealth
        self.__attack = attack
        self.__defense = defense
        self.__speed = speed
    
    
    def getHealth(self):
        return self.__health
    
    def getMaxHealth(self):
        return self.__maxHealth
    
    def getAttack(self):
        return self.__attack
    
    def getDefense(self):
        return self.__defense
    
    def getSpeed(self):
        return self.__speed
    
    def setHealth(self, value):
        self.__health = value
    
    def setMaxHealth(self, value):
        self.__maxHealth = value
    
    def setAttack(self, value):
        self.__attack = value
        
    def setDefense(self, value):
        self.__defense = value
        
    def setSpeed(self, value):
        self.__speed = value