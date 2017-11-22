"""
Python script to create a bounding box polygon.
Uses bounding box SW & NE lat long decimal degrees coordinates as inputs.

Cuurently generates a shapefile and a projection file.
Need to convert output to geojson and test on webmap.

Notes:

- Make the test shapefile area larger for easier viewing on map.
- The current size is tiny and off the west coast of Africa.

Issues:

- The generated shapefile is always the same size and location, not matching inputs.

"""

# Module imports.
import os
import shapefile as shp
from pathlib import Path

# Module Vars

# DFW
# SW_LAT = 32.550058
# SW_LONG = -97.546649
# NE_LAT = 32.987978
# NE_LONG = -97.034774

# New Mexico
SW_LAT = 31.876194
SW_LONG = -108.933343
NE_LAT = 37.048063
NE_LONG = -103.005186

# cellWidth = 10
# cellHeight = 10

fileBaseName = 'bbox_polygon_NM'

current_dir = os.getcwd()
# print('current_dir :: ', current_dir)

absolute_path = os.path.abspath('.')
# print('absolute_path :: ', absolute_path)

base_path = Path(".").resolve()
# print('base_path :: ', base_path)

subdir_path = 'shapefiles/generateBBoxPoly/'
# print('subdir_path :: ', subdir_path)

output_path = os.path.join(str(base_path), str(subdir_path))
# print('output_path :: ', output_path)

# Generate Shapefile.
output_shapefile = os.path.join(output_path, fileBaseName)
print('output_shapefile :: ', output_shapefile)
w = shp.Writer(shp.POLYGON)
w.autoBalance = 1
w.poly(parts=[[[SW_LAT, SW_LONG], [NE_LAT, SW_LONG], [NE_LAT, NE_LONG], [SW_LAT, NE_LONG], [SW_LAT, SW_LONG]]])
w.field('FIRST_FLD','C','100')
w.field('SECOND_FLD','C','100')
w.record('First','Polygon')
w.save(output_shapefile)

# Generate Projection file.
output_projection = os.path.join(output_path, fileBaseName)
print('output_projection :: ', output_projection)
prj = open("%s.prj" % output_projection, "w")
epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
prj.write(epsg)
prj.close()
