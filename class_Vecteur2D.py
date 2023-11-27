import math
class Vecteur2D :
    _nb_vecteurs = 0

    def __init__(self, x=0.0, y=0.0):
        self.__x = x 
        self.__y = y 
        Vecteur2D._nb_vecteurs += 1
    
    def getX(self):
        return self.__x
    
    def setX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setY(self):
        return self.__y
    
    def getNbre(self):
        return self._nb_vecteurs
    
    def ToString(self):
        return " x = "+str(self.getX())+" - y = "+str(self.getY())
    
    def Equals(self, vec):
        if self.__x == vec.getX() and self.__y == vec.getY() :
            return True
        else :
            return False
    
    def Norme(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) 

vec_1 = Vecteur2D(1,2)
vec_2 = Vecteur2D(3,4)
print(vec_1.ToString())
print(vec_1.Equals(vec_2))
print(vec_1.Norme()) 