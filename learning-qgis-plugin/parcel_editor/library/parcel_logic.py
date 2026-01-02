from qgis.core import QgsRasterLayer, QgsProject, edit

class BaseMapLoader:
    """Class to load basemaps"""
    def __init__(self, iface):
        self.iface = iface

    def load_osm(self):
        url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer = QgsRasterLayer(url, "OpenStreetMap", "wms")
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
            self.iface.messageBar().pushInfo("Parcel Editor", "Basemap loaded!")
        else:
            self.iface.messageBar().pushWarning("Parcel Editor", "Failed to load basemap")


class ParcelEditorLogic:
    """Class to handle parcel layer edits"""
    def __init__(self, iface):
        self.iface = iface

    def update_selected_owner(self, new_owner):
        layer = self.iface.activeLayer()
        if not layer:
            self.iface.messageBar().pushWarning("Parcel Editor", "Select a layer first")
            return

        selected = layer.selectedFeatures()
        if not selected:
            self.iface.messageBar().pushInfo("Parcel Editor", "No parcels selected")
            return

        with edit(layer):
            for feat in selected:
                old_owner = feat["owner"]
                feat["owner"] = new_owner
                layer.updateFeature(feat)
                print(f"Parcel {feat['parcel_id']} owner changed from {old_owner} to {new_owner}")
