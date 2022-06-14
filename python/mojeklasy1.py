# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

class Punkt2D:
  def __init__(self,x,y):
      self.x = x
      self.y = y

  def Drukuj(self):
      print("x: ",self.x," y: ", self.y)
      
  def Zeruj(self):
      self.x =0
      self.y =0
     
  def Odcinek(punkt_a,punkt_b):
     a = (punkt_b.x)-(punkt_a.x)
     ap = math.pow(a, 2)
     b = (punkt_b.y)-(punkt_a.y)
     bp =math.pow(b,2)
     c = ap+bp
     print("x punktu a: ",punkt_a.x ,"y punktu a: ",punkt_a.y)
     print("x punktu b: ",punkt_b.x,"y punktu b:",punkt_b.y)
     return  print("Odcinek: ",math.sqrt(c))
      

class Punkt3D(Punkt2D):
    pass
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z = z
        
    def Drukuj(self):
        print("x: ",self.x," y: ",self.y," z: ",self.z)
    
    def Zeruj(self):
        self.x = 0
        self.y = 0
        self.z = 0


        
    
def testy():
 pass
if __name__ == "__main__":
 testy()
 p1 = Punkt2D(5,10)
 p1.Drukuj()
 p2 = Punkt3D(1,2,3)
 p2.Drukuj()
 p3 = Punkt2D(3,4)
 Punkt2D.Odcinek(p1, p3)
 
 
 
 


      