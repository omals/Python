import json
List=open("iris_json.txt").readlines()
print("list having each line of the file as an element :")
print(List)
print("\n")
for i in List:
  print (i)
print("\n")
for i in List:
  if (i['species']=='setosa'):
       print(i)
print("\n")

spec

