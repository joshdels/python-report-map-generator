from qgis.core import QgsProject

project = QgsProject.instance()

# get all layers
layers = project.mapLayers().values()
print(len(layers))

# ----------------

raster_layers = [layer for layer in layers if isinstance(layer, QgsRasterLayer)]

rasters_count = 0
for raster in raster_layers:
    print(raster)
    print("Source:", raster.source()) 
    print("CRS:", raster.crs().authid())
    print("---")
    rasters_count += 1
    
print(f"Num of rasters {raster_layers}")
    