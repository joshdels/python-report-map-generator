from qgis.core import QgsProject, QgsLayoutItemMap, QgsLayoutExporter
from pathlib import Path

"""
This script:
1. Loads a pre-made QGIS layout.
2. Zooms a specified map item to a given layer extent.
3. Exports the layout to an image (PNG).
"""

# -------- CONFIGURATION -----------
CONFIG = {
    "layout_name": "layout",
    "map_item_id": "Map 1",
    "layer_name": "sample_layer",
    "extent_scale": 1.2,
    "export_path": "/home/joshua/Documents/python-report-map-generator/results/",
    "file_name": "image12.png"
}
#-----------------------------------

def get_layout(project, layout_name):
    """Get a layout by name from the project."""
    layout = project.layoutManager().layoutByName(layout_name)
    if layout is None:
        raise ValueError(f"Layout '{layout_name}' not found")
    return layout


def get_map_item(layout, map_item_id):
    """Get a map item from the layout by its ID."""
    map_item = layout.itemById(map_item_id)
    if not isinstance(map_item, QgsLayoutItemMap):
        raise ValueError(f"Map item '{map_item_id}' not found or is not a map")
    return map_item


def get_layer(project, layer_name):
    """Get a layer by name from the project."""
    layers = project.mapLayersByName(layer_name)
    if not layers:
        raise ValueError(f"Layer '{layer_name}' not found")
    return layers[0]


def zoom_map_item_to_layer(map_item, layer, scale=1.0):
    """Zoom the map item to the layer extent with an optional scale."""
    extent = layer.extent()
    extent.scale(scale)
    map_item.zoomToExtent(extent)
    map_item.refresh()


def export_layout(layout, export_path, file_name):
    """Export the layout to an image."""
    output_file = Path(export_path) / file_name
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
