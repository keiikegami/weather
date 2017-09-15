import pygrib
import numpy as np

def get_data(path):
    return pygrib.open(path)

def time_list(grbs):
    time_list = list(set([grb.forecastTime for grb in grbs]))
    return time_list

def point_list(grbs):
    sample = grbs.select(forecastTime=0)[0]
    lats, lons = sample.latlons()
    return lats, lons


# times はinteger list
# lat_pointsはlatitudeを指定するnumpy array
# lon_pointsはlongtitudeを指定するnumpy array
def separation(grbs, times, lat_points, lon_points):
    # separate by forecastTime
    time_index = time_list(grbs)
    lats, lons = point_list(grbs)[0], point_list(grbs)[1]
    
    used_lats = list(set(lats[:, 0]).intersection(set(lat_points)))
    used_lons = list(set(lons[0, :]).intersection(set(lon_points)))
    used_times = list(set(time_index).intersection(set(times)))
    
    # lats, lonsのindexを取ってくる
    initial_lat = lats[0,0]
    iitial_lon = lons[0,0]
    lats_index = [(initial_lat - i)/0.1 for i in used_lats]
    lons_index = [(i - initial_lon)/0.125 for i in used_lons]
    
    if used_times = []:
        print("Use correct times")
        
    elif used_lats = []:
        print("Use correct latitudes")
        
    elif used_lons = []:
        print("Use correct longtitudes")
        
    # とりあえずvalueを取ってくる
    else:
        for time in time_index:
            selected_grb = grbs.select(forecastTime = time)
            for grb in selected_grbs:
                grb.values[lats_index, lons_index]