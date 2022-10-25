import pandas as pd

def env():
    berth_df = pd.read_csv('general_python/datalist/berth_xy.csv')
    berth_x  = berth_df['x [m]'].values
    berth_y  = berth_df['y [m]'].values

    surroundings_df = pd.read_csv('general_python/datalist/surroundings_xy.csv')
    surroundings_x  = surroundings_df['x [m]'].values
    surroundings_y  = surroundings_df['y [m]'].values

    return berth_x, berth_y, surroundings_x, surroundings_y

