import requests

url = f"https://e-commerce-backend-eight-mu.vercel.app/products"
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    #print(json_response)
    print(type(json_response))
    for product in json_response:
        print("Product Name: ",product["name"])
        print("Product Category: ",product["category"])
        print("Product Price: ",product["originalPrice"])
        print("Product year added: ",product["yearAdded"])
        print("\n\n")
except:
    print(f"An error occurred")  

# while True:
