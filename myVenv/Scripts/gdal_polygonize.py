#!C:\Users\Heni\OneDrive\Bureau\projet\myVenv\Scripts\python.exe

import sys

from osgeo.gdal import UseExceptions, deprecation_warn

# import osgeo_utils.gdal_polygonize as a convenience to use as a script
from osgeo_utils.gdal_polygonize import *  # noqa
from osgeo_utils.gdal_polygonize import main

UseExceptions()

deprecation_warn("gdal_polygonize")
sys.exit(main(sys.argv))
