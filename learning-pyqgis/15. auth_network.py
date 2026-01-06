from qgis.core import QgsVectorLayer, QgsProject, QgsNetworkAccessManager
from qgis.PyQt.QtCore import QUrl, QEventLoop
from qgis.PyQt.QtNetwork import QNetworkRequest
import json
import tempfile

# -----------------------------
# CONFIG
# -----------------------------
geojson_url = "http://127.0.0.1:8000/geojson"
token = "alice@example.com"  # your FastAPI token

try:
    # 1 Create request with Authorization header
    request = QNetworkRequest(QUrl(geojson_url))
    request.setRawHeader(b"Authorization", f"Bearer {token}".encode("utf-8"))

    # 2️ Use QGIS network manager to fetch
    nam = QgsNetworkAccessManager.instance()
    reply = nam.get(request)

    # 3️ Wait for the request to finish
    loop = QEventLoop()
    reply.finished.connect(loop.quit)
    loop.exec_()  

    # 4️ Check HTTP status (Qt5 style)
    status = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
    if status != 200:
        raise Exception(f"HTTP error {status}: {reply.errorString()}")

    # 5️ Read the reply as JSON
    geojson_bytes = reply.readAll()
    geojson_str = bytes(geojson_bytes).decode("utf-8")
    geojson_data = json.loads(geojson_str)

    # 6️ Save GeoJSON to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".geojson", mode="w", encoding="utf-8") as tmp_file:
        json.dump(geojson_data, tmp_file)
        tmp_filepath = tmp_file.name

    # 7️ Load the GeoJSON into QGIS
    layer = QgsVectorLayer(tmp_filepath, "Back End Points", "ogr")
    if layer.isValid():
        QgsProject.instance().addMapLayer(layer)
        print("✅ GeoJSON loaded into QGIS!")
    else:
        print("❌ Failed to load layer.")

except Exception as e:
    print(f"❌ Error fetching GeoJSON: {e}")
