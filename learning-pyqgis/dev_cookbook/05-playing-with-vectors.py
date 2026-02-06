# This exercise earlywins of using geopackage

from qgis.core import QgsVectorLayer, QgsProject

# for shapefiles
num_vector = 0
for layer in QgsProject.instance().mapLayers().values():
    
    
    num_vector += 1
    
print(f"Vector Layers inside the qgis gui {num_vector}")