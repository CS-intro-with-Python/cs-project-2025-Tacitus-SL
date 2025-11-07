import requests
import sys

OK, ERR, RST = "\033[32m", "\033[31m", "\033[0m"

url = 'http://127.0.0.1:8080/'
try:
    response = requests.get(url)

    if response.status_code == 200:
        print(f"{OK}Server is working correctly! {RST}")
        print("::notice title=Healthcheck passed::Server responded with 200")
        sys.exit(0)
    else:
        print(f"{ERR}Unexpected response coder: {response.status_code}{RST}")
        print("::error::Unexpected response code from server")
        sys.exit(1)

except Exception as e:
    print(f"{ERR}Failed to connect:{e}{RST}")
    print("::error::Failed to connect to server")
    sys.exit(2)