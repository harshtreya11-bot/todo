import requests
query = input("Enter your Google search query: ")
url = f'https://api.duckduckgo.com/?q={query}&format=json'

print(f"Top search results for '{query}':")
# for result in search(query, num_results=5):
search = requests.get(url)
print(search.status_code)
print(search.json())
print(type(search.json()))
