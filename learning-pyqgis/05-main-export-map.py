from qgis.core import QgsProject, QgsLayoutItemMap, QgsLayoutExporter
from pathlib import Path
import time

CONFIG = {
    "layout_name": "layout",
    "map_item_id": "Map 1",
    "layer_name": "sample_layer",
    "extent_scale": 1.2,
    "export_path": "/home/joshua/Documents/python-report-map-generator/results/",
    "file_name": "image12.png"
}

def get_layout(project, layout_name):
    layout = project.layoutManager().layoutByName(layout_name)
    if not layout:
        raise ValueError(f"Layout '{layout_name}' not found")
    return layout

def get_map_item(layout, map_item_id):
    map_item = layout.itemById(map_item_id)
    if not isinstance(map_item, QgsLayoutItemMap):
        raise ValueError(f"Map item '{map_item_id}' not found or is not a map")
    return map_item

def get_layer(project, layer_name):
    layers = project.mapLayersByName(layer_name)
    if not layers:
        raise ValueError(f"Layer '{layer_name}' not found")
    return layers[0]

def zoom_map_item_to_layer(map_item, layer, scale=1.0):
    extent = layer.extent()
    extent.scale(scale)
    map_item.zoomToExtent(extent)
    map_item.refresh()
    time.sleep(0.2)  # ensures layout registers the new extent

def export_layout(layout, export_path, file_name):
    output_file = Path(export_path) / file_name
    output_file.parent.mkdir(parents=True, exist_ok=True)
    exporter = QgsLayoutExporter(layout)
    result = exporter.exportToImage(str(output_file), QgsLayoutExporter.ImageExportSettings())
    if result != QgsLayoutExporter.Success:
        raise RuntimeError(f"Failed to export layout to {output_file}")
    print(f"Layout exported successfully to: {output_file}")

def main(config):
    project = QgsProject.instance()
    layout = get_layout(project, config["layout_name"])
    map_item = get_map_item(layout, config["map_item_id"])
    layer = get_layer(project, config["layer_name"])

    zoom_map_item_to_layer(map_item, layer, config["extent_scale"])
    export_layout(layout, config["export_path"], config["file_name"])

if __name__ == "__main__":
    main(CONFIG)
