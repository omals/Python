"""

Question 5
Develop a program to read a string and perform the following operations:

* Print all possible substring
* Print all possible substrings of length K
* Print all possible substrings of length K with N distinct characters
* Print all palindrome substrings
"""

#Throughout the program 's' is the string
#k-length of substring   
#n-number of distinct characters

#function to generate substring
def substring(s):                              
  print("\nSubstrings '",s,"'")
  for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
       print(s[i:j],end=" ")    
  print("\t")

#function to generate substring of particular length           
def lengthsubstring(s,k):
   print("\nSubstrings of length :",k,"\n\t",end="")
   for i in range(len(s)+1):
    for j in range(len(s)+1): 
        if len(s[i:j])==k:
            print(s[i:j],end=" ")
   print()

#function to determine the substring with distrinct characters           
def substringdistinct(s,k,n):            
   print("\nSubstrings of length ",k," with ",n," distinct characters\n\t",end="")
   count=0
   for i in range(len(s)+1):
    for j in range(len(s)+1):
        if len(s[i:j])==k:
           sets=set(s[i:j])              #sets-set string
           if len(sets)==n:
             print(s[i:j],end=" ")
             count=1
   if count==0:
      print("There no substrings with ",n," distinct characters in ",k,"length substring")
   print()

#function to find the maximum length substring with n distinct characters
def substringmaxlength(s,n):
   count=0
   temp2=0
   string=[]
   for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):            #sets=set(s[i:j]) 
      if len(set(s[i:j]))==n:
        string.append(s[i:j])
   for i in range(len(string)):
     if(len(string[i])>len(string[-1])):
         print(string[i],end=" ")
         count=1
   #print(maxstring,end=" ")
   if count==0:
      print("There no substrings with ",n," distinct characters in length substring")
   print()

#function to print for palindrome of the string  
def palindrome(s):
   print("\n\tPalindrome substrings")
   for i in range(len(s)+1):
    for j in range(i+1,len(s)):
              sub=s[i:j]                #sub- sub string
              subin=sub[::-1]           #subin- sub string inverse
              if sub==subin:
                 print(subin,end=" ")
   print()

#function where main calling for all function happenning
def main():
  string=str(input("Enter the String:"))
  substring(string)
  length=int(input("\nEnter the length:"))
  lengthsubstring(string,length)
  terms=int(input("\nEnter the number of distinct characters:"))       #terms-to store the numbber of distinct characters
  substringdistinct(string,length,terms)
  print("\nSubstring of length maximum with ",terms," distinct characters\n\t",end="")
  substringmaxlength(string,terms)
  palindrome(string)     

main()                #functions invokation