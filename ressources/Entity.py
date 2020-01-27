class Entity():
    
    """Classe définissant une entité (Monstre ou personnage)
    Elle permettra de définir :
    - Son nom 
    - Réccupérer ses caractéristiques
    """
    
    def __init__(self, name, characteristics): # Notre méthode constructeur
        self.__name = name # __ denotes as a private attribute
        self.__characteristics = characteristics
    
    def getName(self):
        return self.__name
    
    def getCharacteristics(self):
        return self.__characteristics
    
    def setName(self, value):
        self.__name = value
        
    def setCharacteristics(self, value):
        self.__characteristics = value