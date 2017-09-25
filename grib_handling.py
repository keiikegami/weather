import iris
import math
import numpy as np

# the name of coordinates about latitude should be "grid_latitude"
# the name of coordinates about longitude should be "grid_longitude"
# any dimension is o.k.

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
    cube.extract(lat & lon)
    return cube.extract(lat & lon)