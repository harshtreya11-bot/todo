import requests
url= f"https://e-commerce-backend-eight-mu.vercel.app/products"
try:
    response= requests.get(url)
    print(response.status_code)
    json_response = response.json()
    x =input("Enter the Category of product you want to search: ")
    for product in json_response:
        if x == product["category"].lower():
            print("Product Name: ",product["name"])
            print("Product Price: ",product["originalPrice"])
            print("Product Category: ",product["category"])
            print("Product Adding year: ",product["yearAdded"])
            print("\n\n")
except:
    print("Something went wrong")                  

