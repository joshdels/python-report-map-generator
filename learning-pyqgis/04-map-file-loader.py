# Load Data, Zoom then Export to Map as layout

from qgis.core import QgsProject, QgsLayoutItemMap, QgsLayoutExporter

project = QgsProject.instance()

layout = project.layoutManager().layoutByName("layout")
if layout is None:
    raise Exception("Layout not found")
    
map_item = layout.itemById('Map 1')
if map_item is None:
    raise Exception("Map item with ID 'map' is not found")

layer = project.mapLayersByName("sample_layer")[0]

extent = layer.extent()
extent.scale(1.2)
map_item.zoomToExtent(extent)
map_item.refresh()

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(
    "/home/joshua/Documents/python-report-map-generator/results/map16.png", 
    QgsLayoutExporter.ImageExportSettings()
)

map_item.zoomToExtent(extent)
