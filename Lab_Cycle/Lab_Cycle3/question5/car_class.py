import pickle
from fpdf import FPDF

#Designing a class to represent a vehicle
class car:
    #Defining a constructor
    def __init__(self,C_EngNo,C_Model,C_Type,C_Mileage,C_Vendor,C_RegNo,C_OwnName):
        self.C_EngNo = C_EngNo
        self.C_Model = C_Model
        self.C_Type = C_Type
        self.C_Mileage =C_Mileage
        self.C_Vendor = C_Vendor
        self.C_RegNo = C_RegNo
        self.C_OwnName = C_OwnName
    #Function to show the details of the car
    def show(self):
        print(self.C_EngNo,self.C_Model,self.C_Type,self.C_Mileage,self.C_Vendor,self.C_RegNo,self.C_OwnName,sep = "\t")
        print()

#Class to hold the details of several vehicles
class CarDetails:
    def __init__(self):
        self.Car_list = list() #list of car objects
        self.To_write_list = list() #list of car details
    def Load_from_file(self,filename):
        Car_file = open(filename,"rb")
        Car_read_data = pickle.load(Car_file) 
        for i in Car_read_data:
            A = car(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            self.Car_list.append(A)
            self.To_write_list.append(i)
        Car_file.close()
    def add_Car(self,Car):
        self.Car_list.append(Car)
    def show_details(self):
        print("No.\tEngNo.\tModel\tType\tMileage\tVendor\tRegNo.\tOwner\n")
        No = 1
        for CarDetail in self.Car_list:
            print(No,end = "\t")
            No+=1
            CarDetail.show()
            print()
    def Sort_Mileage(self):
        #lambda for sorting
        S_list = sorted(self.To_write_list,key = lambda x : x[3])
        Car_list_index = 0
        self.To_write_list = S_list
        for i in S_list:
            A = car(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            self.Car_list[Car_list_index] = A
            Car_list_index+=1
    def Delete_car(self,RegNo):
        check = False
        del_index = 0
        for i in self.Car_list:
            if i.C_RegNo == RegNo:
                self.Car_list.pop(del_index)
                check = True
            del_index+=1
        if not check:
            print(RegNo,"Does not Exist")
    def Modify_car(self,RegNo,Detail_name,Change_value):
        check = False
        for i in self.Car_list:
            if i.C_RegNo == RegNo:
                check = True
                if i.Detail_name:
                    self.Car_list[i].Detail_name = Change_value
                else:
                    print(Detail_name,"is not a valid detail")
        if not check:
            print(RegNo,"is not a valid parameter")
    def Save_Details(self,filename):
        #Save as a pickle file
        #opening in write binary mode
        Details = open(filename,"wb")
        Details.truncate()
        print(self.To_write_list)
        pickle.dump(self.To_write_list,Details)
        Details.close()
    def Filter_Data(self):
        print("1. Type\n2. RegNo\n 3. Owner Name\n")
        Data_choose = int(input("Choose a Data to filter : "))
    def Create_report(self,filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size = 10)
        pdf.cell(200,10,ln = 2,align = "C",txt = "No.\tEngNo.\tModel\tType\tMileage\tVendor\tRegNo.\tOwner\n")
        
        for entries in self.To_write_list:
            add_text = ""
            for data in entries:
                add_text+=str(data)
                add_text+="\t"
            pdf.cell(200,10,ln = 2,align = "C",txt = add_text)
        pdf.output(filename)

def menu():
    print("1. Show all details of the collection")
    print("2. Sort according to mileage")
    print("3. Add\n4. Delete\n5. Modify")
    print("6. Save the details")
    print("7. Load previous details")
    print("8. Create a pdf report")
    print("9. To Exit")

def main():
    menu()
    Vehicle_list = CarDetails() 
    Continue = True
    while Continue:
        print()
        choice = int(input("Choose an option : "))
        if choice == 1:
            Vehicle_list.show_details()
        elif choice == 2:
            Vehicle_list.Sort_Mileage()
            Vehicle_list.show_details
        elif choice == 3:
            #C_EngNo,C_Model,C_Type,C_Mileage,C_Vendor,C_RegNo,C_OwnName
            print("Enter the details : ")
            d1 = int(input("Engine No  :"))
            d2 = input("Model : ")
            d3 = input("Type  : ")
            d4 = int(input("Mileage : "))
            d5 = input("Vendor : ")
            d6 = int(input("Registration No. :"))
            d7 = input("Owner Name : ")
            to_add_vehicle = car(d1,d2,d3,d4,d5,d6,d7)
            Vehicle_list.add_Car(to_add_vehicle)
        elif choice == 4:
            to_delete_RegNo = int(input("Enter Reg No to delete : "))
            Vehicle_list.Delete_car(to_delete_RegNo)
        elif choice == 5:
            to_modify_RegNo = int(input("Enter Reg No to Modify : "))
            Vehicle_list.Modify_car(to_modify_RegNo)
        elif choice == 6:
            Vehicle_list.Save_Details("data.dat")
        elif choice == 7:
            Vehicle_list.Load_from_file("data.dat")
        elif choice == 8:
            Vehicle_list.Create_report("report.pdf")
        elif choice == 9:
            Continue = False
        else:
            print("Invalid option try again...")

if __name__ == "__main__":
    main()
