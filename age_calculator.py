def age_tracker():
    birth_date= input("Enter your date of Birth :")
    birth_month= input("Enter your month of Birth :")
    birth_year= input("Enter your year of Birth :")
    try:
        print("< Birth Detail add Successfully >")
        print("Entre your Present Date Detail:")
        present_date= input("Enter Present date :")
        present_month= input("Enter Present month :")
        present_year= input("Enter Present year :")
        print("< Present Detail add Successfully >")
        #Calculating Age
        age_year= int(present_year) - int(birth_year)
        age_month= int(present_month) - int(birth_month)
        age_date= int(present_date) - int(birth_date)
        if age_date <0:
            age_month= age_month -1
            age_date= age_date +30
        if age_month <0:
            age_year= age_year  -1
            age_month= age_month +12
        print(f"Your Age is {age_year} Years, {age_month} Months and{age_date} Days")
    except:
        print("Invalid Input, Please enter valid details")
# Age Calculator Entry
while True:
    print("_____________________Welcome to age calculator____________________________")
    print("Entre your DOB and Present Date")
    age_tracker()

# datetime library