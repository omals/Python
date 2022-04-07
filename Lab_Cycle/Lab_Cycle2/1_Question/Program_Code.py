"""Suppose a newly born pair of rabbits, one male and one female, are
put in a field. Rabbits can mate at the age of one month so that at the
end of its second month, a female has produced another pair of
rabbits. Suppose that our rabbits never die and that the female always
produces one new pair every month from the second month.
Develop a program to show a table containing the number of pairs of
rabbits in the first N months."""

def calculate(a):                   #function to calculate the number of rabbits
   n1=1                             #a-months entered by the user
   n2=1
   if a==1:
     display(1,n1)
     return n1
   elif a==2:
     display(1,n1)
     display(2,n2)
     return n2
   else:
    if a!=0:
     display(1,n1)
     display(2,n2)
    
     for i in range(3,a+1):
       n3=n1+n2
       display(i,n3)
       n1=n2
       n2=n3
     return n3
    else:
      print("\nThere is no pair of rabbits are put into the field\n")
      return 0;

def display(j,n3):                  #function to display the values in table format
   print("_"*50)
   print ("\t",j,"\t|\t",n3)
   
     
def main():                         #function take input and give output
   a=int(input("Enter the months: "))       
   print("\n",end='')
   print("-"*50)
   print("\tTABLE OF RABBIT PAIRS")
   print("-"*50)
   print("\tMONTH \t| Number of pair of Rabbits")
   n=calculate(a)                   # n- number of pairs at the end of a months
   print("-"*50)
   print("\nTotal number of Rabbit Pairs at the end of ",a," months is: ",n,"\n")

main()                              #main function to begin the execution
