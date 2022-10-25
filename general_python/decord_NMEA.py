import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

from subroutine import font_set, conversion, read_nmea

data = pd.read_csv("general_python/datalist/20221018_split.csv").values

berth_df = pd.read_csv('general_python/datalist/berth_xy.csv')
berth_x  = berth_df['x [m]'].values
berth_y  = berth_df['y [m]'].values

surroundings_df = pd.read_csv('general_python/datalist/surroundings_xy.csv')
surroundings_x  = surroundings_df['x [m]'].values
surroundings_y  = surroundings_df['y [m]'].values

X = read_nmea.read_GGA_VTG(data)[0]
Y = read_nmea.read_GGA_VTG(data)[1]

fig = plt.figure(figsize = (15.2, 9.6), dpi = 100, linewidth = 0, edgecolor = 'w')
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(X, Y)
# plt.plot(surroundings_y, surroundings_x, color = 'k', linestyle = "-", lw = 0.5)
# plt.plot(berth_y,berth_x, color = 'k',linestyle = '-', lw = 0.5)
# plt.fill_between(surroundings_y, surroundings_x, facecolor = 'k', alpha = 0.3)
# plt.fill_between(berth_y, berth_x, facecolor = 'k', alpha=0.3)
ax1.set_xlim(3.85, 4.2)
ax1.set_ylim(-16.9, -16.7)
ax1.set_aspect('equal')

plt.show()
