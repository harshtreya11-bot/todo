import requests
dog_name = input("Show me all dog breed list :")
url = f"https://dog.ceo/api/breeds/list/all"
print(f"Here is the list of dog breeds :")
try:
    dog_dict = requests.get(url)
    print(dog_dict.status_code)
    json_response = dog_dict.json()
    breed_dict = json_response['message']
    for breed in breed_dict:
        print(breed)
except:
    print("Request failed")

# https://e-commerce-backend-eight-mu.vercel.app/products
