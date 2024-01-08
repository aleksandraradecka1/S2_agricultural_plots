## Analyzing a time-series of Sentinel-2 NDVI values characterizing agricultural plots 🛰️⌚🥕

![](image/landuse_cropped_to_content.jpg)

#### Goal: 
perform a set of geospatial analyses for selected agricultural plots located in Switzerland

#### Data:
- 16 Sentinel-2 images' parts (bands: 'B02', 'B04', 'B08', 'B06' and 'B11'), acquired over Switzerland in 2020 saved in a .zarr format
- agricultural plots with a landuse attribute, saved in a .gpkg format
- checksum file 

#### Research area & time: 
Selected agricultural plots in Switzerland, year of 2022

#### Processing steps:
1. Initial preparation - integrity check
2. Packages import
3. STAC cataloge building
4. Data retrieval via catalogue
5. Raster processing
6. Vector/raster intersection
7. Time-series processing
8. CRS transformation

Prepared by: Aleksandra Radecka <br/>
e-mail: aleksandraradecka@protonmail.com
LinkedIn: https://www.linkedin.com/in/aleksandraradecka/
