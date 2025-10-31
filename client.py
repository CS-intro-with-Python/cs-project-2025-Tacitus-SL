import requests
import sys

url = 'http://127.0.0.1:8080/'
try:
    response = requests.get(url)
    print("Status code: ", response.status_code)
    print("Response: ", response.text)

    if response.status_code != 200:
        print("Some error occured.")
        sys.exit(1)
    print("Everything is fine.")

except Exception as e:
    print("Some error occured.")
    sys.exit(1)