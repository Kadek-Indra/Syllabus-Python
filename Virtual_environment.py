import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

print(f"=== User Information ===")
print (f"Name     : {data['name']}")
print (f"Username : {data['username']}")
print (f"Email    : {data['email']}")
print (f"City     : {data['address']['city']}")
