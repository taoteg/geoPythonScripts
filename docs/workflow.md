# Grid concepts

Polygon grids are grids that are created over a specified extent and stored in a polygon feature class. The grid divides the specified extent into cells so that you can systematically review a large dataset. In the polygon grid, individual grid cells are polygon features that can be attributed and selected.

Before creating the polygon grid, ensure that the data you use meets the following conditions:

- It is stored in a geodatabase that has been created in ArcGIS version 9.3 or higher.
- The X, Y tolerance for the grid must be larger than the geodatabase precision.

# Empty Gridded Shapefile Generation Workflow

1. Prepare inputs
    * SW BoundingBox Lat/Long Point in Degrees Decimal (DD) [FLOAT]
    * NE BoundingBox Lat/Long Point in Degrees Decimal (DD) [FLOAT]
    * cellWidth in meters [INT]
    * cellHeight in meters [INT]
    * output base filename [STRING]


2. Generate Polygon from BoundingBox coordinates.
    * Example.
      - SE BBox = [SW_LAT, SW_LONG]
      - NW BBox = [NE_LAT, NE_LONG]
      - Polygon Coords = [[SW_LAT, SW_LONG], [NE_LAT, SW_LONG], [NE_LAT, NE_LONG], [SW_LAT, NE_LONG], [SW_LAT, SW_LONG]]


3. Subdivide the Polygon into a grid of cells using cellWidth and cellHeight.
4. Generate a new FeatureCollection of Polygons from the cell grid.
5. Join data properties to grid cells by _id field.
6. Write the grid of cells to shapefile or geojson.
7. Generate the .prj file for the correct CRS (EPSG:4326 WGS-84).
8.

# Exisiting Shapefile Data Enhancement Workflow

1. Load existing shapefile from disk.
2. Load new data source to combine with shapefile.
3. Append/update data in shapefile with new data.
4. Write updated shapefile to disk.


# General Libraries for Geospatial Python

- [GDAL](https://pypi.python.org/pypi/GDAL)
- [numpy](https://pypi.python.org/pypi/numpy)
- [pyproj](https://pypi.python.org/pypi/pyproj?)
- [pyshp](https://pypi.python.org/pypi/pyshp)
- [shapely](https://pypi.python.org/pypi/Shapely)
- [shapely (src)](https://github.com/Toblerity/Shapely)
- [Processing.py](http://py.processing.org/)
- [Processing.py (src)](https://github.com/jdf/processing.py)
-

# References for Geospatial Python (and related)

- [GDAL Python API](http://gdal.org/python/)
- [Proj.4](http://proj4.org/)
- [A Guide to NumPy/SciPy Documentation](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
- [Geopandas](http://geopandas.org/)
- [OSGeo](http://www.osgeo.org/)
- [Processing.py on the CLI](http://py.processing.org/tutorials/command-line/)
