import requests
url = f"https://covid19dashboard.mohfw.gov.in/data/datanew.json"
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    print(type(json_response))
    while True:
        x= input("Enter the State for Search the data of State :")
        for datajson in json_response:
            if x== datajson["state_name"].capitalize():
                print("State Name :", datajson["state_name"])
                print("Active Cases :", datajson["active"])
                print("Positive :", datajson["positive"])
                print("Death  :", datajson["death"])
                print("\n\n")
except:        
    print("Data not Found")    
       