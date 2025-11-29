import requests
product_id = input("Enter the product ID you want to search: ")
url = f"https://e-commerce-backend-eight-mu.vercel.app/{product_id}"
print(f"Your product ID {product_id} details are: {url}")
try:
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    print("Product Details:")
    print(f"Name: {json_response['name']}")
    print(f"Price: {json_response['price']}")
    print(f"Description: {json_response['description']}")
except:
    print(f"An error occurred")  

# while True:
