from qgis.core import QgsProject, QgsApplication
import os

project = QgsProject.instance()

save_path = r"C:\Users\deleo\Downloads\project.qgz"

project.clear()

success=project.write(save_path)

if success:
    print(f"Successfully created empty QGIS project file: {save_path}")
else:
    print("Failed to save the project file.")
    
# its all about read, write and path for the qgis file