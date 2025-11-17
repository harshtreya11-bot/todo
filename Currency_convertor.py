 


def INR_to_USD(USD_val):
    INR_val = USD_val*88.69
    print(USD_val,"USD is equal to :",INR_val,"INR")
def USD_to_INR(INR_val):
    USD_val = INR_val/88.69
    print(INR_val,"INR is equal to :",USD_val,"USD")
def INR_to_EUR(EUR_val):
    INR_val = EUR_val/0.0097
    print(EUR_val,"EUR is equal to :",INR_val,"INR") 
def EUR_to_INR(INR_val):
    EUR_val = INR_val*0.0097
    print(INR_val,"INR is equal to :",EUR_val,"EUR") 
def INR_to_JPY(JPY_val):
    INR_val = JPY_val/1.74
    print(JPY_val,"JPY is equal to :",INR_val,"INR") 
def JPY_to_INR(INR_val):
    JPY_val = INR_val*1.74
    print(INR_val,"INR is equal to :",JPY_val,"JPY") 
def INR_to_AED(INR_val):
    AED_val = INR_val*0.041
    print(INR_val,"INR is equal to :",AED_val,"AED") 
def AED_to_INR(AED_val):
    INR_val = AED_val/0.041
    print(AED_val,"AED is equal to :",INR_val,"INR") 
while True:
    print("____________________________________Welcome to Currency Converter_________________________________________________________________")
    print(" ")
    print("____________________________________Press 1. for INR to USD_______________________________________________________________________")
    print("____________________________________Press 2. for USD to INR_______________________________________________________________________")
    print("____________________________________Press 3. for INR to EUR_______________________________________________________________________")
    print("____________________________________Press 4. for EURO to INR_______________________________________________________________________")
    print("____________________________________Press 5. for INR to JPY_______________________________________________________________________")
    print("____________________________________Press 6. for JPY to INR_______________________________________________________________________")
    print("____________________________________Press 7. for INR to AED_______________________________________________________________________")
    print("____________________________________Press 8. for AED to INR_______________________________________________________________________")
    print("____________________________________Press 9. for Exit the Converter_______________________________________________________________________")
    x= int(input("_______________press the following value for any action__________ :"))
    if x==1:
        print("____________________________________________Welcome to INR to USD Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        USD_to_INR(y)
    elif x==2:
        print("____________________________________________Welcome to USD to INR Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        INR_to_USD(y)
    elif x==3:
        print("____________________________________________Welcome to INR to EUR Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        EUR_to_INR(y)
    
    elif x==4:
        print("____________________________________________Welcome to EUR to INR Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        INR_to_EUR(y) 
    elif x==5:
        print("____________________________________________Welcome to INR to JPY Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        JPY_to_INR(y)

    elif x==6:
        print("____________________________________________Welcome to JPY to INR Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        INR_to_JPY(y)

    elif x==7:
        print("____________________________________________Welcome to INR to AED Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        INR_to_AED(y)
    elif x==8:
        print("____________________________________________Welcome to AED to INR Converter________________________________________________")
        y= int(input("Entre the amount you want to change:"))
        AED_to_INR(y)
    elif x==9:
        print("____________________________________________Thanyou for choosing this app :)________________________________________________")  
        break
    else:
        print("____________________________________________You enter a wrong value :(______________________________________________________")                       