#!C:\Users\Heni\OneDrive\Bureau\projet\myVenv\Scripts\python.exe

import sys

from osgeo.gdal import UseExceptions, deprecation_warn

# import osgeo_utils.ogrmerge as a convenience to use as a script
from osgeo_utils.ogrmerge import *  # noqa
from osgeo_utils.ogrmerge import main

UseExceptions()

deprecation_warn("ogrmerge")
sys.exit(main(sys.argv))
