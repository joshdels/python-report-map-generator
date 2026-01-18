import os
import shutil
from qgis.core import (
    QgsProject,
    QgsVectorFileWriter,
    QgsMapLayer,
    QgsRasterPipe,
    QgsRasterFileWriter
)

# ---------------------------
# SETTINGS
# ---------------------------
downloads = os.path.expanduser("~/Downloads")
project_name = "MyQGISProject_Offline"
output_folder = os.path.join(downloads, project_name)

vector_gpkg = os.path.join(output_folder, "Vectors.gpkg")
raster_folder = os.path.join(output_folder, "rasters")
basemap_folder = os.path.join(output_folder, "basemaps")

# Create directories
os.makedirs(output_folder, exist_ok=True)
os.makedirs(raster_folder, exist_ok=True)
os.makedirs(basemap_folder, exist_ok=True)

project = QgsProject.instance()
layers = project.mapLayers().values()

# ---------------------------
# EXPORT LAYERS
# ---------------------------
for layer in layers:
    layer_name = layer.name().replace(" ", "_")

    # ---------- VECTOR ----------
    if layer.type() == QgsMapLayer.VectorLayer:
        # Ensure even in-memory layers are exported
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = "GPKG"
        options.layerName = layer_name
        options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer

        QgsVectorFileWriter.writeAsVectorFormatV2(
            layer,
            vector_gpkg,
            project.transformContext(),
            options
        )
        print(f"Vector → {layer_name}")

    # ---------- RASTER ----------
    elif layer.type() == QgsMapLayer.RasterLayer:
        raster_path = os.path.join(raster_folder, f"{layer_name}.tif")

        pipe = QgsRasterPipe()
        pipe.set(layer.dataProvider().clone())

        writer = QgsRasterFileWriter(raster_path)
        writer.writeRaster(
            pipe,
            layer.width(),
            layer.height(),
            layer.extent(),
            layer.crs()
        )
        print(f"Raster → {layer_name}")

    # ---------- BASEMAP / XYZ / WMS ----------
    elif layer.providerType() in ("xyz", "wms", "wmts"):
        cache_path = os.path.join(basemap_folder, layer_name)
        os.makedirs(cache_path, exist_ok=True)

        # Try to copy tile cache if exists
        uri = layer.dataProvider().dataSourceUri()
        if os.path.exists(uri):
            shutil.copytree(uri, cache_path, dirs_exist_ok=True)
            print(f"Basemap cached → {layer_name}")
        else:
            print(f"Basemap online → {layer_name} (no local cache)")

    else:
        print(f"Skipped → {layer_name}")

# ---------------------------
# SAVE PROJECT INTO FOLDER
# ---------------------------
project_path = os.path.join(output_folder, "project.qgz")
project.write(project_path)

print("\nDONE! Offline folder ready at:")
print(output_folder)
