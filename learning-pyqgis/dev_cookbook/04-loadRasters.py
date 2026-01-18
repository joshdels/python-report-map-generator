# This exercise loading of multiple rasters and reading them

from qgis.core import QgsRasterLayer, QgsProject


def load_single_raster():
    """Load single raster file"""
    raster_path = r"C:\Users\deleo\Downloads\test\Unisan_dtm_1m.tif"
    rlayer = QgsRasterLayer(raster_path, "unisan")

    if not rlayer.isValid():
        print("Layer fail to load")
    else:
        QgsProject.instance().addMapLayer(rlayer)
        print("Layer Loaded!")
        

# load_single_raster()
    
# Looping a folder for the raster layer
def load_raster_from_folder():
    """Load multiple Raster File"""
    raster_folder = r"C:\Users\deleo\Downloads\test"
    raster_extensions = [".tif", ".tiff", ".jpg", ".jpeg", ".png"]

    for filename in os.listdir(raster_folder):
        if any(filename.lower().endswith(ext) for ext in raster_extensions):
            raster_path = os.path.join(raster_folder, filename)
            layer_name = os.path.splitext(filename)[0]
            rlayer = QgsRasterLayer(raster_path, layer_name)
            
            if not rlayer.isValid():
                print(f"Failed to load: {filename}")
            else:
                QgsProject.instance().addMapLayer(rlayer)
                print(f"Loaded raster: {filename}")
                
# load_raster_from_folder()



# Chekcing 
for layer in QgsProject.instance().mapLayers().values():
    if isinstance(layer, QgsRasterLayer):
        print(layer)
        
        source = layer.source()
        provider = layer.providerType()
        crs = layer.crs()
        
        print(source)
        print(provider)
        print(crs)
    


