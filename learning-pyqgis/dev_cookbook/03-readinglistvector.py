# This exercise earlywins of using geopackage

from qgis.core import QgsVectorLayer, QgsProject

# for shapefiles
for layer in QgsProject.instance().mapLayers().values():
    if isinstance(layer, QgsVectorLayer):
        print(layer)
        
        source = layer.source()
        provider = layer.providerType()
        
        print(layer.source())
        print(layer.providerType())
        print(layer.crs())