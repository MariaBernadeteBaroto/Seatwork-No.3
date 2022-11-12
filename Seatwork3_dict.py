# Seatwork-3

# Display a menu of options

print("********************************")
print()
print("          MENU          ")
print()
print(" 1 -->  Add an item    ")
print(" 2 -->  Search         ")
print(" 3 -->  Exit (y/n)      ")  
print()
print()
print("*******************************")

# Dictionary

Tracing_list = {
}

while True:
    # Allow user to select item in the menu
    choice1= input("Choose option displayed on menu(1-3): ")

    # Implement Option 1
    if choice1.casefold() == "1" :
        data1=input("What is your name? ")
        data2=input("What is your age? ")
        data3=input("What is your address? ")
        data4=input("Please type your contact number: ")
        data5=input("Do you experience any symptoms in the past 7 days?(y/n): ")
        data6=input("In case of emergency, who will be your contact person? ")
        data7=input("What is your relationship to your contact person? ")
        data8=input("Please type the contact number of your contact person: ")
        
        dict_name = {
            "Age"       : data2,
            "Address"   : data3,
            "Contact Number"  : data4,
            "Symptoms" : data5,
            "Contact Person" : data6,
            "Relationship to Contact Person" : data7,
            "Contact number of Contact Person" :data8
        }
        Tracing_list[data1] = dict_name
        print(Tracing_list)

    # Implement Option 2
    if choice1.casefold() == "2":
        search=input("Please enter the name: ")
        search_dict=Tracing_list.get(search)
        for key, value in search_dict.items():
            print(key, ":", value)
    
    # Implement Option 3
    if choice1.casefold() == "3":
        choice=input("Are you sure you want to exit?(y/n)")
        if choice == "y":
            print()
            print("************************")
            print()
            print("      Thank you         ")
            print()
            print("************************")
            break
        
