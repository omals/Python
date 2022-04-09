

"""Question 2
Develop a program to read the three sides of two triangles and calculate the area of both. 
Define a function to read the three sides and call it. Also, define a function to calculate the area. 
Print the total area enclosed by both triangles and each triangle's contribution (%) towards it
s=(a+b+c)/2
A=sqrt(s(s-a)(s-b)*(s-c))
"""

#function to input the side
def side():
  side=int(input("Enter the side:"))
  return (side)

#function to calculate area
def area():
  s1=side()                      #s1,s2,s3- three sides of triangle
  s2=side()
  s3=side()
  semip=(s1+s2+s3)*0.5           #semip=semiperimeter of teh triangle
  calculation=semip*(semip-s1)*(semip-s2)*(semip-s3)
  a=calculation**0.5
  print("Area",a)
  return a

#function to calculate the contribution of each triangle
def contribution(a1,a2):                         #a1- area of first triangle
  print("Total",(a1+a2))                         #a2- area of second triangle
  con1=(a1/(a1+a2))*100                          #con1- contribution of first triangle
  con2=(a2/(a1+a2))*100                          #con2- contribution of second triangle
  print("Contribution of first triangle",con1)
  print("Contribution of second triangle",con2,"\n")

#function to be invoked
def main():
  print("\nArea of TRIANGLE")
  print("TRIANGLE 1 : ")
  area1=area()
  print("\nTRIANGLE 2 : ")
  area2=area()
  print("\nContribution of each trianglr")
  contribution(area1,area2)

main()                                            #function invokation
