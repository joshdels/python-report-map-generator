# Difference between iface and qgisproject

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsMessageLog,
    Qgis,
    QgsProcessing Feedback,
)

file_path = "D:/1. PROJECT/Mangroves CDO/data/AOI.geojson"
mangroves = QgsVectorLayer(file_path, "AOI", "ogr")

if not mangroves.isValid():
    print("Layer failed to load!")
    QgsMessageLog.logMessage(
        "Layer failed to load!", level=Qgis.Critical, tag="Nooooo"
    )
    
else: 
    QgsProject.instance().addMapLayer(mangroves)
    QgsMessageLog.logMessage(
        "Joshua is here loaded successfully!", level=Qgis.Info, tag="Nooooo"
    )

try: 
    layer = iface.activeLayer()

    if layer:
        layer.removeSelection()
        # layer.selectAll()
        iface.mapCanvas().zoomToSelected(layer)
except NameError:
    QgsMessageLog.logMessage(
        "iface is not available (running outside QGIS GUI)", \
        level=QgsMessageLog.INFO, tag="Error"
    )
