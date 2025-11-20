import requests
word = input("Entre the word you want to search :")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
print(f"Your word {word} means :")
dict = requests.get(url)
print(dict.status_code)
print(dict.json())
print(type(dict.json()))

# age = 18

# print("Your age is", age, ". You are teenager")
# print(f"Your age is {age}. You are tenagr")

# url2 = "https://www.google.com/search?q=search"

# search = input("Entre your query you want to search :")
# print(f"your query = {search}  is :")
# see = requests.get(url2)
# print(see.status_code)
# print(dict.json())
# print(type(dict.json()))
