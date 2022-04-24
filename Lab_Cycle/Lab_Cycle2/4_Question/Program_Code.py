"""Write a program to create a class Box with data members length, breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume. Create a list of N boxes with random measurements and print the
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
 
   # def volume(self):                                 #member function to calculate volume
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
       print("\tRatio  : ",r)
       return r

def maxratio(r):                                    #function to find and check the maximum Volume:Area ratio
  if len(r["ratio"])==0 :                           #exception
   print("Complete")
  else:
   templistratio=list(r["ratio"])		      #'templistratio'-temporary list of ratio from the dictionary
   maximum=max(templistratio)			      #'maximum'-Maximum ratio of the list of ratio 'r'
   tempi=templistratio.index(maximum)               #'tempi'-Temporary index of maximum ratio in te list
   templistkey=list(r["Key"])                       #'templistkey'-Temporary list of key from the dictionary
   keyvalue=(int(templistkey[tempi]))               #'keyvalue'-to get the key value at that index
   print("\nMaximum volume:area ratio  for ",end="")
   if keyvalue== 1 :
     print ("Cube. Value = ",templistratio[tempi],"\n")
   elif keyvalue==2:
     print ("Square Prism. Value = ",templistratio[tempi],"\n")
   elif keyvalue==3:
     print ("Rectangular Prism. Value = ",templistratio[tempi],"\n")
   else:
     print("Something Wrong","\n")
    
def cube():
  cube=[]                                         #cube list declaration for dimensions
  cube.append(random.randint(1,1000))             #random values assigned
  print("_"*70)
  print("Cube : dimensions = ",cube)
  cube_obj=Box(cube[0])                           #object declaration constructor with one argument is called
  cube_obj.area()
  #cube_obj.volume()
  cube_obj.display()
  return(cube_obj.ratio())

def squareprisum():
  square=[]                                       #square prism list declaration for dimensions
  for i in range(2):
    square.append(random.randint(1,1000))        #random values assigned
  print("_"*70)
  print("square Prism : dimensions = ",square)
  squarep_obj=Box(square[0],square[1])           #object declaration constructor with two arguments is called
  squarep_obj.area()
  #squarep_obj.volume()
  squarep_obj.display()
  return(squarep_obj.ratio())

def rectangularprisum():
  rectangle=[]                                    #rectangle list declaration for dimensions
  for i in range(3):
     rectangle.append(random.randint(1,1000))    #random values assigned
  print("_"*70)
  print("Rectangular Prism : dimensions = ",rectangle)
  rectangularp_obj=Box(rectangle[0],rectangle[1],rectangle[2])    #object declaration with three arguments called
  rectangularp_obj.area()
  #rectangularp_obj.volume()
  rectangularp_obj.display()
  return(rectangularp_obj.ratio())
  
def main():                                       #main function
 n=int(input("\nEnter the number of BOX required : "))
 ratio={"ratio":[],"Key":[]}                                     #ratio dictionary of list declaration for storing the values
 if(n<=2):
   for k in range(0,n,2):					   #loop to create box of different shapes with random values
    if(k<n):
      ratiov=cube()
      ratio["ratio"].append(ratiov)                             #appending the values to the dictionary
      ratio["Key"].append("1")
      k=k+1
    if(k<n):
      ratiov=squareprisum()
      ratio["ratio"].append(ratiov)
      ratio["Key"].append("2")
      k=k+1
 else:
   for k in range(0,n,3):
    if(k<n):
      ratiov=cube()
      ratio["ratio"].append(ratiov)
      ratio["Key"].append("1")
      k=k+1
    if(k<n):
      ratiov=squareprisum()
      ratio["ratio"].append(ratiov)
      ratio["Key"].append("2")
      k=k+1
    if(k<n):
      ratiov=rectangularprisum()
      ratio["ratio"].append(ratiov)
      ratio["Key"].append("3")
      k=k+1
    
 print("_"*70)
 maxratio(ratio)                                #function call
  
main()
