import requests
url = "https://prices.finmachines.dev/api/v1/prices/history/ercot/VL_8080"
token = "b8213403aef548073ccb7669d3ac7d510b8f9a85"
headers = {"Authorization": f"Token {token}"}
data = { "years": [2019]}
response = requests.request("GET", url=url, headers=headers, params=data)
path = f"/home/f3nix/Downloads/dirty/check.zip"

if response.status_code == 200:
    with open(path, 'wb') as f:
        f.write(response.content)
    print("Data downloaded successfully.")
else:
    print("Error downloading:", response.status_code)