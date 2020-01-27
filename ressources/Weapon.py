
class Weapon():
    """
    Classe définissant une arme (principalement les charactéristiques qu'elle apporte au joueur).
    """
    
    def __init__(self, name, weight, characteristics): # Notre méthode constructeur
        self.__name = name
        self.__weight = weight
        self.__characteristics = characteristics
    
    def getName(self):
        return self.__name
    
    def getWeight(self):
        return self.__weight
    
    def getCharacteristics(self):
        return self.__characteristics
    
    def setName(self, value):
        self.__name = value
    
    def setWeight(self, value):
        self.__weight = value
    
    def setCharacteristics(self, value):
        self.__characteristics = value