
class Inventory:
    """
    Classe définissant l'inventaire de notre personnage.
    Celui-ci possède une taille (size) qui définit le nombre d'emplacement (slot) de ce dernier.
    Chaque objet possède un poid ce qui permet de gérer le nombre d'objet maximum portable par 
    le personnage. Par exemple, s'il trouve une arme qui possède un poid de 3, l'inventaire verra
    son nombre d'emplacement passer à x -3.
    """
    
    def __init__(self, size): # Notre méthode constructeur
        self.__size = size
        self.__slotList = []
        
    def getSize(self):
        return self.__size
    
    def getSlotList(self):
        return self.__slotList
    
    def setSize(self, value):
        self.__size = value
    
    def setSlotList(self, value):
        self.__slotList = value
        