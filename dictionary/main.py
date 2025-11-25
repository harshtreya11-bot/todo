import requests
word = input("Entre the word you want to search :")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
print(f"Your word {word} means :")

try:
    dict = requests.get(url)
    print(dict.status_code)
    json_response = dict.json()
    # first_dict = json_response[0]
    # print(first_dict)
    # second_dict = json_response[0]["meanings"]
    # print(second_dict)
    second_dict = json_response[0]["meanings"]
    for item in second_dict:
        print(second_dict[2:4])
        
    

except:
    print("Request failed")

# age = 18

# print("Your age is", age, ". You are teenager")
# print(f"Your age is {age}. You are tenagr")

