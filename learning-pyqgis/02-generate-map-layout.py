# Generate map images, save the curated layout first
from qgis.core import QgsProject, QgsLayoutExporter

project = QgsProject.instance()
manager = project.layoutManager()

layout = manager.layoutByName('layout')

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(
    "/home/joshua/Documents/python-report-map-generator/results/map12.png", 
    QgsLayoutExporter.ImageExportSettings()
)