"""

Question 3
Develop a program to read the employee's name, code, and basic pay
and calculate the gross salary, deduction, and net salary according to
the following conditions. Define a function to find each of the
components. Finally, generate a payslip.
Gross Salary (GS) : BP + DA + HRA + MA
Deduction (D): PT + PF + IT
Net Salary = GS – D
"""

#function to include the details of the employee
def detail():
  name=str(input("Enter the name \t  : "))
  code=int(input("Enter the code \t  : "))
  basic_pay=float(input("Enter the basic pay:"))
  return (name,code,basic_pay)

#function to calculate the Gross Salary
def gross_salary(bp,da,hra,ma):
  gs=bp+da+hra+ma                              #gs- Gross Salary value
  print("Gross salary\t =  \t",gs)
  return gs

#function to claculate Deduction
def deduction(pt,pf,it):                       
  d=pt+pf+it                                   #d- Deduction value
  print("Deduction \t = \t",d)
  return d

#function to calculate the Net Salary
def net_salary(BP,DA,HRA,MA,PT,PF,IT):
  GS=gross_salary(BP,DA,HRA,MA)                #invoke the function gross_salary and return value to GS
  D=deduction(PT,PF,IT)                        #invoke the function deduction and return value to D
  ns=  GS-D                                    #ns- store value of Net Salary
  print("Net Salary \t = \t",ns)

#function to display the input details of employee
def display(nam,cod,basicpay):                 #nam-name   cod-code   
  print("Name of the employee \t :",nam)
  print("Code of the employee \t :",cod)
  print("Basic pay of the employee:",basicpay)

#function from which all other functions are invoked
def main():
  print("Enter the details of the employee.")
  n,c,bp=detail()                             #n-name   c-code      bp-Basic Pay of the employee
  print("\tPay list")
  display(n,c,bp)                             #invoke Display function
  if(bp<10000):
    net_salary(bp,5,2.5,500,20,8,0)           #invoke net_salary function
  elif(bp<30000 and bp>=10000):
    net_salary(bp,7.5,5,2500,60,8,0)
  elif(bp<50000 and bp>=30000):
     net_salary(bp,11,7.5,5000,60,11,11)
  else:
    net_salary(bp,25,11,7000,80,12,20)

main()                        #invoke the main function