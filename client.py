import requests
import sys

url = 'http://127.0.0.1:8080/88'
try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Server is working correctly!")
        sys.exit(0)
    else:
        print(f"Unexpected response from server: {response.text}")
        sys.exit(1)

except Exception as e:
    print(f"Client failed to connect to server:{e}")
    sys.exit(2)