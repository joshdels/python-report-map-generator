import os

from qgis.core import (
    Qgis,
    QgsProject,
    QgsPathResolver
)

full_path = os.path.expanduser('~/Downloads/test/')

print(full_path)  # C:\Users\deleo\Downloads\test.qgs
print(os.path.exists(full_path))  # True if the file exists

filename = "test2.ggz"
# Save the project
project.write(f"{full_path}/{filename}")