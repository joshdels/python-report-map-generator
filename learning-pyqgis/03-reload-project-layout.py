# Reuse the QGIS layout

from qgis.core import QgsProject, QgsLayoutExporter

# reloading the project
project = QgsProject.instance()
project.read
project.read("/home/joshua/Documents/python-report-map-generator/learning-pyqgis/practice.qgz")

# read the layout
layout = project.layoutManager().layoutByName("layout")

# export as map layout
exporter = QgsLayoutExporter(layout)
exporter.exportToImage(
    "/home/joshua/Documents/python-report-map-generator/results/map3.png",
    QgsLayoutExporter.ImageExportSettings()
)