import requests

BASE_URL = "https://topmapsolutions.com/api/v1"

# ---- Login ----
data = {"username": "admin", "password": "admin1234"}
r = requests.post(f"{BASE_URL}/login/", json=data)
token = r.json().get("token")
print("Token:", token)

# ---- Get Projects ----
headers = {"Authorization": f"Token {token}"}
r = requests.get(f"{BASE_URL}/projects/", headers=headers)
print(r.json())

# ---- Logout ----
r = requests.post(f"{BASE_URL}/logout/", headers=headers)
print(r.json())
