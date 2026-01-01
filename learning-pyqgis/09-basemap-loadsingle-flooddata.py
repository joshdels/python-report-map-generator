# add load base map
# import the gpkg file and paint it with styles

import os
from qgis.core import (
    QgsVectorLayer,
    QgsRasterLayer,
    QgsProject
)

file = "study"
DATA_DIR = f"/home/joshua/Documents/python-report-map-generator/data/{file}/"
STYLE = "/home/joshua/Documents/python-report-map-generator/data/styles/flood_styles.qml"

project = QgsProject.instance()

# -------------------------------------------------------------------
# ADD BASE MAP (XYZ TILE)
# -------------------------------------------------------------------
osm_url = (
    "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
    "&zmin=0&zmax=19"
)

basemap = QgsRasterLayer(osm_url, "OSM", "wms")

if basemap.isValid():
    project.addMapLayer(basemap)
else:
    print("Failed to load basemap")

# -------------------------------------------------------------------
# LOAD GPKG FILES AND APPLY STYLE
# -------------------------------------------------------------------
for file in os.listdir(DATA_DIR):
    if not file.lower().endswith(".gpkg"):
        continue

    path = os.path.join(DATA_DIR, file)
    name = "Flood Risk 100 yr"

    layer = QgsVectorLayer(path, name, "ogr")
    if not layer.isValid():
        print(f"Failed to load {file}")
        continue

    # load styles
    ok, err = layer.loadNamedStyle(STYLE)
    if not ok:
        print(f"Style error on {name}: {err}")

    # add layer to project
    project.addMapLayer(layer)
    layer.triggerRepaint()

    print(f"Loaded {file}")
