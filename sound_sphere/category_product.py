import requests
url = f"https://e-commerce-backend-eight-mu.vercel.app/products"
categories = []
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()

    for product in json_response:
            product_already_present = False
            if product["category"]not in categories:
                categories.append(product["category"])
                
    print(categories)        
except:                                              
    print("Try again")

