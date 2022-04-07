"""Write a program to create a parent class, 3DShapes, with methods
printVolume() and printArea(), which prints the Volume and Area,
respectively. Create classes Cylinder and Sphere by inheriting
3DShapes class. Using these child classes, calculate and print the
volume and area of a cylinder and sphere."""


class threeD_shape:                                            #Base class threeD_shape
  def printVolume(self):
    print("\tVolume :",self.volume)
  def printArea(self):
    print("\tArea   :",self.area)
    
class Cylinder(threeD_shape):                                  #Derived class Cylinder
   def __init__(self,r,h):                                     #Constructor
     self.radius=r
     self.height=h
   def calculateA(self):                                       #member function to calculate area of cylinder
     self.area=(2*3.14*self.radius*self.height)+(2*3.14*self.radius**2)
     threeD_shape.printArea(self)
   def calculateV(self):                                       #member function to calculate volume of cylinder
     self.volume=3.14*self.radius**2*self.height
     threeD_shape.printVolume(self)                           #call to the base class function
   
class Sphere(threeD_shape):                                   #Derived class Sphere
   def __init__(self,r):                                      #Constructor
     self.radius=r
   def calculateA(self):                                      #member function to calculate area of sphere
     self.area=4*3.14*self.radius**2
     threeD_shape.printArea(self)
   def calculateV(self):                                      #member function to calculate volume of sphere
     self.volume=4/3*3.14*self.radius**3
     threeD_shape.printVolume(self)                          #call to the base class function
     
def main():
   print("_"*70)
   print("Cylinder : ")
   cylinderR=int(input("\tEnter the Radius : "))
   cylinderH=int(input("\tEnter the Height : "))
   cylinder_obj=Cylinder(cylinderR,cylinderH)               #Object declaration 
   cylinder_obj.calculateA()
   cylinder_obj.calculateV()
   print("_"*70)
   print("Sphere : ")
   sphereR=int(input("\tEnter the Radius : "))
   sphere_obj=Sphere(sphereR)                              #Object declaration
   sphere_obj.calculateA()
   sphere_obj.calculateV()
   print("_"*70)
   
main()                                                     #beginning of program execution
