# Loading BaseMap

from qgis.core import QgsRaster, QgsProject

url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
name = "OpenStreetMap"
basemap = QgsRasterLayer(url, name, "wms")

if not basemap.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(basemap)
    print("Basemap added successfully!")
    