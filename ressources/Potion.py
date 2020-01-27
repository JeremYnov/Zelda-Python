
class Potion():
    """
    Classe définissant une potion et l'effet de chacune lors de leur utilisation.
    """
    
    def __init__(self, name, weight): # Notre méthode constructeur
        self.__name = name
        self.__weight = weight
    
    def getName(self):
        return self.__name
    
    def getWeight(self):
        return self.__weight
    
    def setName(self, value):
        self.__name = value
        
    def setWeight(self, value):
        self.__weight = value