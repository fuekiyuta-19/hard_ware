import pandas as pd
import numpy as np

def env():
    berth_df = pd.read_csv('general_python/datalist/berth_xy.csv')
    berth_x  = berth_df['x [m]'].values
    berth_y  = berth_df['y [m]'].values

    surroundings_df = pd.read_csv('general_python/datalist/surroundings_xy.csv')
    surroundings_x  = surroundings_df['x [m]'].values
    surroundings_y  = surroundings_df['y [m]'].values

    return berth_x, berth_y, surroundings_x, surroundings_y

def ship_shape(x, y, psi, ship_type) : # 0:esso, 1:takaoki
    pp_takaoki_CSV  = pd.read_csv('general_python/datalist/input_CSV_VR/principal_particulars_cement.csv', index_col = 0)
    esso_lpp        = 3.0
    esso_breadth    = 0.48925
    takaoki_lpp     = pp_takaoki_CSV.at['lpp', 'value']
    takaoki_breadth = pp_takaoki_CSV.at['breadth', 'value']
#     ref
    if ship_type == 0 :
        lpp     = esso_lpp
        breadth = esso_breadth
        
    elif ship_type == 1 :
        lpp       = takaoki_lpp
        breadth   = takaoki_breadth

    shipshape_Y   = np.array([-lpp / 2, lpp / 4, lpp / 2, lpp / 4, -lpp / 2, -lpp / 2])
    shipshape_X   = np.array([-breadth / 2, -breadth / 2, 0, breadth / 2, breadth / 2, -breadth / 2])
    pole_r        = np.empty(6)
    pole_theta    = np.empty(6)
    pole_r[:]     = (shipshape_X[:] ** 2 + shipshape_Y[:] ** 2) ** (1 / 2)
    pole_theta[:] = np.arctan2(shipshape_Y[:],shipshape_X[:])

    x_fix = np.cos(pole_theta[:] + psi) * pole_r[:] + x
    y_fix = np.sin(pole_theta[:] + psi) * pole_r[:] + y

    return x_fix, y_fix