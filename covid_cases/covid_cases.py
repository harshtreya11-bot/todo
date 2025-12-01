import requests
url = f"https://covid19dashboard.mohfw.gov.in/data/datanew.json"
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    print(type(json_response))
    for datajson in json_response:
        print("State Name :", datajson["state_name"])
        print("Active Cases :", datajson["active"])
        print("Positive :", datajson["positive"])
        print("Death  :", datajson["death"])
        print("\n\n")
except:        
    print("Data not Found")       