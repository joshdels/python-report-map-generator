import requests
import json  # for pretty printing

BASE_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# 1️⃣ Login
# --------------------------------------------------
login_resp = requests.post(
    f"{BASE_URL}/token",
    data={
        "username": "alice@example.com",
        "password": "alice123"
    }
)

login_resp.raise_for_status()
token = login_resp.json()["access_token"]
print("✅ Token:", token)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# --------------------------------------------------
# 2️⃣ Test protected endpoint
# --------------------------------------------------
data_resp = requests.get(f"{BASE_URL}/mydata", headers=headers)
data_resp.raise_for_status()
print("✅ User Data:", data_resp.json())

# --------------------------------------------------
# 3️⃣ Get GeoJSON
# --------------------------------------------------
geojson_resp = requests.get(f"{BASE_URL}/geojson", headers=headers)
geojson_resp.raise_for_status()
geojson = geojson_resp.json()

print("✅ GeoJSON fetched")
print("Feature count:", len(geojson["features"]))

# --------------------------------------------------
# 4️⃣ Print full features nicely
# --------------------------------------------------
print("\n--- Features ---")
for i, feature in enumerate(geojson["features"], start=1):
    geom = feature.get("geometry")
    props = feature.get("properties")
    print(f"{i}: Geometry: {geom}, Properties: {props}")
