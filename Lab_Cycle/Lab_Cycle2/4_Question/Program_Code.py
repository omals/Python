"""Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio."""

import random
class Box:                                              #class box defined                             
    count=0                                             #with the initial value of data members
    length = 0.0
    breadth = 0.0
    height = 0.0
    volume = 0.0
    area=0.0
    def __init__(self,*args):                           #Constructor
        if(len(args)==1):
          self.length=args[0]
          self.count=0
        elif(len(args)==2):
          self.length = args[0]
          self.height = args[1]
          self.count=1
        elif(len(args)==3):
          self.length=args[0]
          self.breadth=args[1]
          self.height=args[2]
          self.count=2
        else:
          print("Constructor out of Scope.")
    def area(self):                                    #member function to calculate area
        if(self.count==0):
          self.area=6*self.length**2
        elif(self.count==1):
          self.area=(2*self.length**2)+(4*self.length*self.height)
        elif(self.count==2):
          self.area=2*(self.breadth*self.length+self.height*self.length+self.height*self.breadth)
        else:
          print("Something went worry") 
 
    def volume(self):                                 #member function to calculate volume
        if(self.count==0):
          self.volume=self.length**3
        elif(self.count==1):
          self.volume=(self.length**2)*self.height
        elif(self.count==2):
          self.volume=self.length*self.breadth*self.height
        else:
          print("Something went worry") 
 
    def display(self):                               #member function to display the calculated values
       print("\tArea   : ",self.area)
       print("\tVolume : ",self.volume)
        
    def ratio(self):
       r=self.volume/self.area
       return r

def maxratio(r):                                    #function to find and check the maximum Volume:Area ratio
  m=max(r)                                          # m-maximum value in the list 'r'
  i=r.index(m) 
  print("\nMaximum volume:area ratio  for ",end="")
  if(i==0):
    print ("Cube. Value = ",r[i],"\n")
  elif(i==1):
    print ("Square Prism. Value = ",r[i],"\n")
  elif(i==2):
    print ("Rectangular Prism. Value = ",r[i],"\n")
  else:
    print("\nSomething Wrong","\n")
    
def main():                                       #main function
  ratio=[]                                        #ratio array declaration
  cube=[]                                         #cube array declaration
  cube.append(random.randint(1,1000))             #random values assigned
  
  print("_"*70)
  print("Cube : dimensions = ",cube)
  cube_obj=Box(cube[0])                           #object declaration constructor with one argument is called
  cube_obj.area()
  cube_obj.volume()
  cube_obj.display()
  ratio.append(cube_obj.ratio())

  square=[]
  for i in range(2):
    square.append(random.randint(1,1000))        #random values assigned
  print("_"*70)
  print("square Prism : dimensions = ",square)
  squarep_obj=Box(square[0],square[1])           #object declaration constructor with two arguments is called
  squarep_obj.area()
  squarep_obj.volume()
  squarep_obj.display()
  ratio.append(squarep_obj.ratio())

  rectangle=[]                                   #rectangle array declaration
  for i in range(3):
     rectangle.append(random.randint(1,1000))    #random values assigned
  print("_"*70)
  print("Rectangular Prism : dimensions = ",rectangle)
  rectangularp_obj=Box(rectangle[0],rectangle[1],rectangle[2])    #object declaration with three arguments called
  rectangularp_obj.area()
  rectangularp_obj.volume()
  rectangularp_obj.display()
  ratio.append(rectangularp_obj.ratio())
  print("_"*70)
  maxratio(ratio)                                #function call
  
main()
