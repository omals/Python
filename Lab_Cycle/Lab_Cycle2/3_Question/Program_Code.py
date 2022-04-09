"""Read the file 'iris.json' as a text file :
  1. Create a list having each line of the file as an element
  2. Convert it into a list of dictionary objects.
  3. Show the details of all flowers whose species is "setosa".
  4. Print the minimum petal area and max sepal area in each species
  5. Sort the list of dictionaries according to the total area are sepal and petal."""

import json
List1=open("iris.json","r")                             
List=List1.readlines() 			          #The file elements as list elements
print("\nlist having each line of the file as an element :")
print("Type of the list ",type(List))
print("Type of each element in the list ",type(List[0]),"\n")
for i in List:                                          #Each element in the List 
   print (i)
print("\n")
List1.close()

List2=open("iris.json",'r')                            
dictionary=json.load(List2) 				 #list of dictionary
print("List of Dictionary")
print("Type of  list\t",type(dictionary))
print("Type of each element in list ",type(dictionary[0]),"\n")
for i in dictionary:	
     print(i)
     
print("\nAll flowers whose species is setosa\n")
for i in dictionary:					  #'i' is the dictionary element in the list
  if (i['species']=='setosa'):
       print(i)
print("\n")
						         #For finding Maximum sepalarea and minimum petalarea of each species 
l_species=[]                                           
areas1=[]					        
areap1=[]
areas2=[]
areap2=[]
areas3=[]
areap3=[]
for i in dictionary:
  if(i['species'] not in l_species):                               #list to sort the species
       l_species.append(i['species'])
for i in dictionary:                                                 
  if(i['species']==l_species[0]):                                    
      areas1.append(i['sepalLength']*i['sepalWidth'])              #calculate sepal area of species of setosa
      areap1.append(i['petalLength']*i['petalWidth'])              #calculate petal area of species of setosa
      
  elif(i['species']==l_species[1]):
      areas2.append(i['sepalLength']*i['sepalWidth'])	     #calculate sepal area of species of versicolor
      areap2.append(i['petalLength']*i['petalWidth'])              #calculate petal area of species of versicolor
      
  elif(i['species']==l_species[2]):
      areas3.append(i['sepalLength']*i['sepalWidth'])             #calculate sepal area of species of virginica
      areap3.append(i['petalLength']*i['petalWidth'])             #calculate petal area of species of virginica
      
print(l_species[0],":")
print("\tMaximum sepal area : ",max(areas1))
print("\tMinimum petal arae : ",min(areap1))
print(l_species[1],":")
print("\tMaximum sepal area : ",max(areas2))
print("\tMinimum petal arae : ",min(areap2))
print(l_species[2],":")
print("\tMaximum sepal area : ",max(areas3))
print("\tMinimum petal arae : ",min(areap3))

print("\nList of Dictionaries including the 'TotalArea' : \n")     
for i in dictionary:
  stotal=(i['sepalLength']*i['sepalWidth'])
  ptotal=(i['petalLength']*i['petalWidth'])
  totalarea=ptotal+stotal					       #Total area of each species 
  i.update({'TotalArea' : totalarea})
for i in dictionary: 
  print(i)              
print("\n")  
  
sorteddictionary=(sorted(dictionary,key=lambda i:i['TotalArea']))   #sorting the dictionaries in order of Totalarea
print("List of Dictionary being Sorted by the Total area : \n")
for i in sorteddictionary:
   print(i)   
      
      
      
List2.close()
      
      
      
