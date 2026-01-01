# import the gpkg file and paint it with styles

import os
from qgis.core import QgsVectorLayer, QgsProject

DATA_DIR = "/home/joshua/Documents/python-report-map-generator/data/flood_clean/"
STYLE = "/home/joshua/Documents/python-report-map-generator/data/styles/flood_styles.qml"

# file checking
for file in os.listdir(DATA_DIR):
    if not file.lower().endswith(".gpkg"):
        continue
        
    path = os.path.join(DATA_DIR, file)
    name = os.path.splitext(file)[0]
    
    layer = QgsVectorLayer(path, name, "ogr")
    if not layer.isValid():
        print(f"Failed to load {file}")
        continue
    
    # load styles
    ok, err = layer.loadNamedStyle(STYLE)
    if not ok:
        print(f"Syle error on {name}: {err}")
    
    # qgis load then style
    QgsProject.instance().addMapLayer(layer)
    layer.triggerRepaint()
    
    print(f"Loaded {file}")
