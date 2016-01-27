# main.py
# Januari 18

import os,os.path
import mapnik

from shapely.geometry import *
import fiona

import os
os.chdir('/home/user/git/TwoLocations')
print os.getcwd()

os.mkdir('./shapefile')
os.mkdir('./output')

#import our function
from createshape import createpointshape

# WUR Gaia: 51.986936, 5.666768
# Best city of the Netherlands: 51.842103, 5.859398
point1 = Point([(5.666768, 51.986936)])
point2 = Point([(5.859398,  51.842103)])

# Execute our own function to create shapefile with two points.
print createpointshape(point1, point2)


import zipfile
zip_ref = zipfile.ZipFile("./data/ne_110m_land.zip", 'r')
zip_ref.extractall("./data")
zip_ref.close()


#file with symbol for point
file_symbol=os.path.join("data","marker.png")

#First we create a map
map = mapnik.Map(800, 400) #This is the image final image size

#Lets put some sort of background color in the map
map.background = mapnik.Color("steelblue") # steelblue == #4682B4 

#Create the rule and style obj
r = mapnik.Rule()
s = mapnik.Style()

polyStyle= mapnik.PolygonSymbolizer(mapnik.Color("darkred"))
pointStyle = mapnik.PointSymbolizer(mapnik.PathExpression(file_symbol))
r.symbols.append(polyStyle)
r.symbols.append(pointStyle)

s.rules.append(r)
map.append_style("mapStyle", s)

# Adding point layer
layerPoint = mapnik.Layer("pointLayer")
layerPoint.datasource = mapnik.Shapefile(file=os.path.join("shapefile",
                                        "twopoints.shp"))

layerPoint.styles.append("mapStyle")

#adding polygon
layerPoly = mapnik.Layer("polyLayer")
layerPoly.datasource = mapnik.Shapefile(file=os.path.join("data",
                                        "ne_110m_land.shp"))
layerPoly.styles.append("mapStyle")

#Add layers to map
map.layers.append(layerPoly)
map.layers.append(layerPoint)

#Set boundaries 
boundsLL = (1.3,51.979, 8.306,53.162  ) #(minx, miny, maxx,maxy)
map.zoom_to_box(mapnik.Box2d(*boundsLL)) # zoom to bbox

# Write map to file TwoPointsMap.png
mapnik.render_to_file(map, os.path.join("output",
                                        "TwoPointsMap.png"), "png")
print "All done - check output/TwoPointsmap.png"
