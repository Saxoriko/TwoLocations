# -*- coding: utf-8 -*-
"""

@author: saxoriko
"""

from shapely.geometry import *
import fiona

def createpointshape(point1, point2):

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
        
    return "Shapefile created!"