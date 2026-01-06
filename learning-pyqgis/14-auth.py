import requests
from qgis.core import QgsVectorLayer, QgsProject
import json
import tempfile
import os

# 1️ Login to get token
login_url = "http://127.0.0.1:8000/token"
login_data = {"username": "alice@example.com", "password": "alice123"}

login_resp = requests.post(login_url, data=login_data)
token = login_resp.json()["access_token"]
print("Token:", token)

# 2️ Fetch GeoJSON from FastAPI
geojson_url = "http://127.0.0.1:8000/geojson"
headers = {"Authorization": f"Bearer {token}"}

geojson_resp = requests.get(geojson_url, headers=headers)
geojson_data = geojson_resp.json()
print("GeoJSON data:", geojson_data)

# 3️ Save GeoJSON to temporary file (text mode)
with tempfile.NamedTemporaryFile(delete=False, suffix=".geojson", mode="w", encoding="utf-8") as tmp_file:
    json.dump(geojson_data, tmp_file)
    tmp_filepath = tmp_file.name

# 4 Load GeoJSON into QGIS
layer = QgsVectorLayer(tmp_filepath, "BackEnd Points", "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print("GeoJSON layer added to QGIS!")
else:
    print("Failed to load layer.")

# Optional: delete temp file if you want
# os.remove(tmp_filepath)
