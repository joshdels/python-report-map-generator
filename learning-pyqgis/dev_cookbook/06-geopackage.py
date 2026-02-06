
from qgis.core import QgsVectorLayer, QgsVectorFileWriter, QgsProject

gpkg_path = r"C:\Users\deleo\Downloads\project.gpkg"

# Create a minimal memory layer
layer = QgsVectorLayer("Point?crs=EPSG:4326", "init_layer", "memory")

# Save it to GeoPackage
options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.layerName = "init_layer"
options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile

res, err = QgsVectorFileWriter.writeAsVectorFormatV2(layer, gpkg_path, QgsProject.instance().transformContext(), options)
if res == QgsVectorFileWriter.NoError:
    print("GeoPackage created (with dummy layer)")