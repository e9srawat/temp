import requests

iso = "ercot"
node_type = "busbar"
curve="dam"
years=["2017","2018","2019","2020","2021","2022","2023","2024"]
token = "df0d4404991c3885a213283d4b50cc0b386b353e"
headers = {"Authorization": f"Token {token}"}


# year = "2019"
# url = f"https://prices.finmachines.dev/api/v1/prices/history/boss/realdirty/{iso}/{node_type}/{curve}/"
# path = f"/home/f3nix/Downloads/dirty/isone.zip"
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     with open(path, 'wb') as f:
#         f.write(response.content)
#     print("Data downloaded successfully.")
# else:
#     print("Error downloading:", response.status_code)
        

for year in years:
    url = f"https://prices.finmachines.dev/api/v1/prices/history/boss/realdirty/{iso}/{node_type}/{curve}/?year={year}"
    path = f"/home/f3nix/Downloads/dirty/isone_{year}.zip"
    response = requests.get(url, headers=headers)
# print(response.content)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print("Data downloaded successfully.")
    else:
        print("Error downloading:", response.status_code)
        