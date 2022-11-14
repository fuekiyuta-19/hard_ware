import pandas as pd
import numpy as np

def env():

    berth_df = pd.read_csv('general_python/datalist/input_CSV_VR/berth_xy.csv')
    berth_x  = berth_df['x [m]'].values
    berth_y  = berth_df['y [m]'].values

    surroundings_df = pd.read_csv('general_python/datalist/input_CSV_VR/surroundings_xy.csv')
    surroundings_x  = surroundings_df['x [m]'].values
    surroundings_y  = surroundings_df['y [m]'].values

    return berth_x, berth_y, surroundings_x, surroundings_y


def ship_shape(x, y, psi, ship_type) : # 0:esso, 1:takaoki

    pp_takaoki_CSV  = pd.read_csv('general_python/datalist/input_CSV_VR/principal_particulars_cement.csv', index_col = 0)
    esso_lpp        = 3.0
    esso_breadth    = 0.48925
    takaoki_lpp     = pp_takaoki_CSV.at['lpp', 'value']
    takaoki_breadth = pp_takaoki_CSV.at['breadth', 'value']

    if ship_type == 0 :
        lpp = esso_lpp
        bre = esso_breadth
        
    elif ship_type == 1 :
        lpp = takaoki_lpp
        bre = takaoki_breadth

    shipshape_X   = np.array([-lpp / 2,  lpp / 4, lpp / 2, lpp / 4, -lpp / 2, -lpp / 2])
    shipshape_Y   = np.array([-bre / 2, -bre / 2,    0,    bre / 2,  bre / 2, -bre / 2])
    pole_r        = np.empty(6)
    pole_theta    = np.empty(6)
    pole_r[:]     = (shipshape_Y[:] ** 2 + shipshape_X[:] ** 2) ** (1 / 2)
    pole_theta[:] = np.arctan2(shipshape_X[:], shipshape_Y[:])
    psi_rad       = psi - np.arctan(1) * 2.0

    # y_fix = (np.cos(pole_theta[:] + psi_rad) * pole_r[:]) + y
    # x_fix = (np.sin(pole_theta[:] + psi_rad) * pole_r[:]) + x

    y_fix = (np.cos(pole_theta[:] + psi) * pole_r[:]) + y
    x_fix = (np.sin(pole_theta[:] + psi) * pole_r[:]) + x

    return x_fix, y_fix


def ship_shape_dist(dist, psi):

    pp_takaoki_CSV  = pd.read_csv('general_python/datalist/input_CSV_VR/principal_particulars_cement.csv', index_col = 0)

    lpp = pp_takaoki_CSV.at['lpp', 'value']
    bre = pp_takaoki_CSV.at['breadth', 'value']

    shipshape_Y   = np.array([-lpp / 2,  lpp / 4, lpp / 2, lpp / 4, -lpp / 2, -lpp / 2])
    shipshape_X   = np.array([-bre / 2, -bre / 2,    0,    bre / 2,  bre / 2, -bre / 2])
    pole_r        = np.empty(6)
    pole_theta    = np.empty(6)
    pole_r[:]     = (shipshape_X[:] ** 2 + shipshape_Y[:] ** 2) ** (1 / 2)
    pole_theta[:] = np.arctan2(shipshape_Y[:], shipshape_X[:])

    x_fix = np.cos(pole_theta[:] + psi) * pole_r[:] - (dist + 0.165) * np.cos(psi)
    y_fix = np.sin(pole_theta[:] + psi) * pole_r[:]

    return x_fix, y_fix