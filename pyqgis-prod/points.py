from qgis.core import (
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsProject
)

def create_point_layer(
    lon: float,
    lat: float,
    name: str = "Area of Interest",
    crs: str = "EPSG:4326"
):
    """
    Create a memory point layer with a single point.
    Default layer name is 'Area of Interest'.
    """
    layer = QgsVectorLayer(f"Point?crs={crs}", name, "memory")
    provider = layer.dataProvider()

    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(lon, lat)))

    provider.addFeatures([feature])
    layer.updateExtents()
    QgsProject.instance().addMapLayer(layer)

    return layer
