from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY

class PointGeometry:
    def __init__(self):
        pass

    def create_layer_point(self, x, y, layer_name="Points" ):
        layer = QgsVectorLayer(
            "Point?crs=EPSG:4326",
            layer_name,
            "memory"
        )

        if not layer.isValid():
           raise RuntimeError("Failed to create a layer")
        
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))

        provider = layer.dataProvider()
        provider.addFeature(feature)
        
        layer.updateExtents()

        QgsProject.instance().addMapLayer(layer)
        
        return layer