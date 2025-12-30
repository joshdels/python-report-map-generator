# Load Data, Zoom then Export to Map as layout

from qgis.core import QgsProject, QgsLayoutItemMap, QgsLayoutExporter

'''
This file load a layout (prefabricated) zoom a base item, export to the path
'''

# -------- CONFIGURATION -----------
LAYOUT_NAME = "layout"
MAP_ITEM_ID = "Map 1"
LAYER_NAME = "sample_layer"
EXTENT_SCALE = 1.2
EXPORT_PATH = "/home/joshua/Documents/python-report-map-generator/results/"
FILE_NAME = "image12.png"
#-----------------------------------


project = QgsProject.instance()

layout = project.layoutManager().layoutByName(LAYOUT_NAME)
if layout is None:
    raise Exception(f"'{LAYOUT_NAME}' not found")
    
map_item = layout.itemById(MAP_ITEM_ID)
if map_item is None:
    raise Exception(f"Map item with ID '{MAP_ITEM_ID}' is not found")

layer = project.mapLayersByName(LAYER_NAME)[0]

extent = layer.extent()
extent.scale(EXTENT_SCALE)

map_item.zoomToExtent(extent)
map_item.refresh()

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(
    f"{EXPORT_PATH}{FILE_NAME}", 
    QgsLayoutExporter.ImageExportSettings()
)
