import iris
import math
import numpy as np

# the name of coordinates about latitude should be "grid_latitude"
# the name of coordinates about longitude should be "grid_longitude"
# any dimension cube.

# read data from pp format file
def readpp(filename):
    try:
        cube = iris.load(filename)
        return cube
    except ValueError:
        print "unable to load this file"
        
# write data from pp format file
def readpp(cube, savepath):
    try:
        iris.save(cube, savepath)
    except ValueError:
        print "unable to save this file"


# grid points after changing resolution
def lat_id(cube, drop_rate):
    lat_num = len(cube.coord("grid_latitude").points)
    span = math.ceil((lat_num - math.ceil((lat_num*drop_rate))) /(math.ceil((lat_num*drop_rate)) + 1))
    last = math.ceil((lat_num - span)/(span+1))
    last_ind = span + (last - 1)*(span + 1)
    
    drop_ind = np.linspace(span, last_ind, last)
    return list(set(range(lat_num)).difference(set(drop_ind)))

def lon_id(cube, drop_rate):
    lon_num = len(cube.coord("grid_longitude").points)
    span = math.ceil((lon_num - math.ceil((lon_num*drop_rate))) /(math.ceil((lon_num*drop_rate)) + 1))
    last = math.ceil((lon_num - span)/(span+1))
    last_ind = span + (last - 1)*(span + 1)
    
    drop_ind = np.linspace(span, last_ind, last)
    return list(set(range(lon_num)).difference(set(drop_ind)))

# resolution shange
def change_resolution(cube, drop_rate):
    constlat = iris.Constraint(grid_latitude = cube.coord("grid_latitude").points[lat_id(cube, drop_rate)])
    constlon = iris.Constraint(grid_longitude = cube.coord("grid_longitude").points[lon_id(cube, drop_rate)])
    return cube.extract(constlat & constlon)

# extraction
def extraction(cube, latstart, latend, lonstart, lonend):
    con1 = iris.Constraint(grid_latitude=lambda cell: latstart <= cell <= latend)
    con2 = iris.Constraint(grid_longitude=lambda cell: lonstart <= cell <= lonend)
    return cube.extract(con1 & con2)