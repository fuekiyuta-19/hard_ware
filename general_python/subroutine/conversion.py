import numpy as np
import math

theta_berth = 1.143942290114601e+02
berth_rad   = np.deg2rad(theta_berth)
mid2gps     = 0.0

def convert(lat_td, lon_td):
    # Input value format:
    # 13531.484779127149817, 3449.365327040533202
    
    lat_z = 34 + 49.365327040533202 / 60
    lon_z = 135 + 31.484779127149817 / 60
    tran  = np.pi * 6378137 / 180

    lat = math.modf(lat_td / 100)[1] + math.modf(lat_td / 100)[0] * 100 / 60
    lon = math.modf(lon_td / 100)[1] + math.modf(lon_td / 100)[0] * 100 / 60
    
    y_gps = (lat - lat_z) * tran
    x_gps = (lon - lon_z) * tran * np.cos(lat * np.pi / 180)

    Y1 = y_gps
    X1 = x_gps
    
    X = X1 * np.cos(berth_rad) - Y1 * np.sin(berth_rad)
    Y = X1 * np.sin(berth_rad) + Y1 * np.cos(berth_rad)
    
    return X, Y