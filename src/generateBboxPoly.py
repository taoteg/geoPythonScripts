"""
Python script to create a bounding box polygon.
Uses bounding box SW & NE lat long decimal degrees coordinates as inputs.
"""

# Module imports.
import shapefile as shp

# Module Vars
# TEST COORDS: -97.546649, 32.550058 & -97.034774, 32.987978
SW_LAT = 32.550058
SW_LONG = -97.546649
NE_LAT = 32.987978
NE_LONG = -97.034774
# cellWidth = 10
# cellHeight = 10
fileBaseName = 'bbox_polygon'

# Example.
# """
w = shp.Writer(shp.POLYGON)
w.autoBalance = 1
# w.poly(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
# [[SW_LAT, SW_LONG], [NE_LAT, SW_LONG], [NE_LAT, NE_LONG], [SW_LAT, NE_LONG], [SW_LAT, SW_LONG]]
w.poly(parts=[[[SW_LAT, SW_LONG], [NE_LAT, SW_LONG], [NE_LAT, NE_LONG], [SW_LAT, NE_LONG], [SW_LAT, SW_LONG]]])
w.field('FIRST_FLD','C','100')
w.field('SECOND_FLD','C','100')
w.record('First','Polygon')
# w.save('shapefiles/test/polygon')
w.save(fileBaseName)

# Projection file.
prj = open("%s.prj" % fileBaseName, "w")
epsg = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]'
prj.write(epsg)
prj.close()
# """

# Generate grid file.
"""
w = shp.Writer(shp.POLYGON)
w.autoBalance = 1
w.field('ID')
w.field('NAME')
# id = 0
# feature_name = ""
# w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.poly(shapeType=3, parts=[[[122,37,4,9], [117,36,3,4]], [[115,32,8,8], [118,20,6,4], [113,24]]])
w.save(fileBaseName)
"""
