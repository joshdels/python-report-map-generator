import sys
from pathlib import Path

# Adjust path to your project
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT / "pyqgis_prod"))

from points import create_point_layer

# Create point layer
layer = create_point_layer(123.8854, 10.3157, name="Cebu Point")
