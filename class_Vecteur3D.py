from class_Vecteur2D import Vecteur2D
import math
class Vecteur3D(Vecteur2D):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self.__z = z
    
    def getZ(self):
        return self.__z
    
    def setZ(self):
        return self.__z
    
    def ToString(self):
        return " x = "+str(self.getX())+" - y = "+str(self.getY())+" - z = "+str(self.__z)
    
    def Equals(self , vec):
        if self.getX() == vec.getX() and  self.__y == vec.getY() and self.__z == vec.getZ():
            return True
        else :
            return False

    def Norme(self):
        return math.sqrt(self.getX() ** 2 + self.getY() ** 2 + self.__z ** 2)
    
vec_3 = Vecteur3D(5,6,7)
vec_4 = Vecteur3D(8,9,10)
print(vec_3.ToString())
print(vec_4.Equals(vec_3))
print(vec_3.Norme())  