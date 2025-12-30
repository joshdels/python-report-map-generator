# Load Vector Layer
layer = QgsVectorLayer("/home/joshua/Documents/python-report-map-generator/shapefiles/layer_black", "sample_layer", "ogr")
QgsProject.instance().addMapLayer(layer)
layer.isValid()

for feature in layer.getFeatures():
    attrs = feature.attributes()
    geom = feature.geometry()
    print(attrs, geom.area())