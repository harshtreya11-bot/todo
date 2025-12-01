import requests
url = f"https://e-commerce-backend-eight-mu.vercel.app/products"
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    x= int(input("Enter the Prince in which you want to Search the products : "))
    for product in json_response:
        if x== product["originalPrice"]:
            print("Product Name: ",product["name"])
            print("Product Price: ",product["originalPrice"])
            print("Product Category: ",product["category"])
            print("Product Added year: ",product["yearAdded"])
            print("\n\n")
                
except:
    print("Something went wrong")   
    print("Try again :(")         
