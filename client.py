import requests

url = 'http://127.0.0.1:8080/'

resp_hello = requests.get(f"{url}/hello")
print("Hello:", resp_hello.json())

username = 'Svyat'
resp_user = requests.get(f"{url}/user/{username}")
print("USER:", resp_user.json())

params = {'q': 'python'}
resp_search = requests.get(f"{url}/search", params=params)
print("SEARCH:", resp_search.json())