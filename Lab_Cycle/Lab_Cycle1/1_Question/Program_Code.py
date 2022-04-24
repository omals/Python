"""
Question 1
Write a program to read a four-digit number and find its
a. Sum of digits
b. Reverse
c. Difference between the products of digits at the odd position and the product of digits at the even position.
"""

def arithemetic_operations():
	num=int(input("Enter the four digit number:"))
	t=num
	sum=0
	reverse=0                               #reverse to store the reverse number

	reminder1=num%10                        #reminder1- store the last digit
	reverse=(reverse*10)+reminder1
	num=num//10

	reminder2=num%10                        #reminder2- store the last second digit
	reverse=(reverse*10)+reminder2
	num=num//10

	reminder3=num%10                        #reminder3- store the second digit
	reverse=(reverse*10)+reminder3                   
	num=num//10

	reminder4=num%10                        #reminder4- store the first digit
	reverse=(reverse*10)+reminder4
	num=num//10
	sum=reminder4+reminder3+reminder2+reminder1
	difference=(reminder2*reminder4)-(reminder1*reminder3)
	
	print("Sum=",sum)                        #print the sum of the digits
	print("Reverse = ",end="")		  #print the reverse of the input number
	if(t%10==0):				  
		while(t!=0):
	  		if(t%10==0 and t//10):
	    			print("0",end="")                   
	  		t=t//10
	print(reverse) 
	print("Difference=",difference)          #print the difference between the products
	
arithemetic_operations()
