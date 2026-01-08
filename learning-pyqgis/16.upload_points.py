import json
import requests
from qgis.core import QgsProject, QgsVectorLayer

# -----------------------------
# CONFIG
# -----------------------------
API_BASE = "http://127.0.0.1:8000"
USERNAME = "alice@example.com"
PASSWORD = "alice123"

# Name of the layer in QGIS to upload
LAYER_NAME = "Points"

# -----------------------------
# 1️⃣ Login to get token
# -----------------------------
login_resp = requests.post(f"{API_BASE}/token", data={
    "username": USERNAME,
    "password": PASSWORD
})
login_resp.raise_for_status()
token = login_resp.json()["access_token"]
print("✅ Token acquired:", token)

headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# -----------------------------
# 2️⃣ Find layer in QGIS
# -----------------------------
layer = None
for lyr in QgsProject.instance().mapLayers().values():
    if lyr.name() == LAYER_NAME:
        layer = lyr
        break

if layer is None:
    raise Exception(f"Layer '{LAYER_NAME}' not found in QGIS project.")

print(f"✅ Found layer '{layer.name()}' with {layer.featureCount()} features.")

# -----------------------------
# 3️⃣ Convert layer to GeoJSON
# -----------------------------
geojson = {
    "type": "FeatureCollection",
    "features": []
}

for feat in layer.getFeatures():
    geom = feat.geometry()
    if geom is None:
        continue

    # Only handle Points for simplicity
    if geom.type() != 0:  # 0 = Point
        continue

    coords = geom.asPoint()
    properties = {field.name(): feat[field.name()] for field in layer.fields()}

    geojson["features"].append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [coords.x(), coords.y()]
        },
        "properties": properties
    })

print(f"✅ Converted {len(geojson['features'])} features to GeoJSON.")

# -----------------------------
# 4️⃣ Upload GeoJSON to API
# -----------------------------
upload_resp = requests.post(f"{API_BASE}/upload/geojson",
                            headers=headers,
                            json=geojson)
upload_resp.raise_for_status()

result = upload_resp.json()
print("✅ Upload response:", result)
