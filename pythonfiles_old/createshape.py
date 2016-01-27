# -*- coding: utf-8 -*-
"""

@author: saxoriko
"""

from shapely.geometry import *
import fiona


# WUR Gaia: 51.986936, 5.666768
# Best city of the Netherlands: 51.842103, 5.859398
point1 = Point([(5.666768, 51.986936)])
point2 = Point([(5.859398,  51.842103)])

# Define a polygon feature geometry with one attribute
schema = {
    'geometry': 'Point',
    'properties': {'id': 'int'},
}


# Write a new Shapefile
with fiona.open('./shapefile/twopoints.shp', 'w', 'ESRI Shapefile', schema) as c:
    ## If there are multiple geometries, put the "for" loop here
    c.writerecords([{
        'geometry': mapping(point1),
        'properties': {'id': 1}},{
        'geometry': mapping(point2),
        'properties': {'id': 2}}
    ])
    
    