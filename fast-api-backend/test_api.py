import requests

# Login
login_resp = requests.post("http://127.0.0.1:8000/token", data={
    "username": "alice@example.com",
    "password": "alice123"
})
token = login_resp.json()["access_token"]
print("Token:", token)

headers = {"Authorization": f"Bearer {token}"}

data_resp = requests.get("http://127.0.0.1:8000/mydata", headers=headers)
print("User Data:", data_resp.json())

geojson_resp = requests.get("http://127.0.0.1:8000/geojson", headers=headers)
print("User GeoJSON Data:", geojson_resp.json())




