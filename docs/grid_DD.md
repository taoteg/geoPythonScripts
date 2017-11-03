# grid_DD.py Description and Usage

## Intended Use

For use in manipulating grids based on Decimal Degrees (DD).

- Create a Shapefile
- Read Shapefile
- Edit Shapefile
  - Delete
  - Add
  - Modify
  - Reproject
  - Combine
- Write Shapefile
- Write GeoJSON file

### Inputs

__Type__              : The kind of inputs to expect. Enumerated as follows:

    'bbox'      // Bounding Box Extents using SW & NE Coordinates
    'esri-shp'  Load an existing Shapefile

__SW & NE Extents__   : The coordinates in decimal degrees for the two pionts southe west (lower left) and north east (upper right) that define the extents of the bounding box area.


__Path to Shapefile__ : The relative file path or absolute file path to the shapefile being loaded.


__Actions__ 
