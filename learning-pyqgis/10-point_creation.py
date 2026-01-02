import sys
sys.path.append("/home/joshua/document/python")

from points import create_point_layer

create_point_layer(
    name="Manila",
    lon=120.9842,
    lat=14.5995
)

create_point_layer(
    name="Cebu",
    lon=123.8854,
    lat=10.3157
)

create_point_layer(
    name="Davao",
    lon=125.6128,
    lat=7.1907
)
