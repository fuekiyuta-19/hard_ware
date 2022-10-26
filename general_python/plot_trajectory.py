import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from subroutine import font_set, plottool

filepath = "general_python/datalist/"
dataname = ["TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_38_49",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_42_05",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_45_18",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_47_37"]
datanum = 2
data = pd.read_csv(filepath + dataname[datanum] + ".csv")

fig = plt.figure(figsize = (15.2, 9.6), dpi = 100, linewidth = 0, edgecolor = 'w')
ax1 = fig.add_subplot(1, 1, 1)

for j in range(len(data)):
    if j % 5 == 0:
        X, Y = plottool.ship_shape(data['y_raw'].values[j], data['x_raw'].values[j], np.rad2deg(data['psi_raw_rad'].values[j]), 1)
        ax1.plot(X, Y, color = "r", linestyle = "-", lw = 0.5)
    else:
        pass
        
ax1.scatter(X, Y)
ax1.plot(plottool.env()[3], plottool.env()[2], color = 'k', linestyle = "-", lw = 0.5)
ax1.plot(plottool.env()[1], plottool.env()[0], color = 'k', linestyle = '-', lw = 0.5)
ax1.fill_between(plottool.env()[3], plottool.env()[2], facecolor = 'k', alpha = 0.3)
ax1.fill_between(plottool.env()[1], plottool.env()[0], facecolor = 'k', alpha = 0.3)
ax1.set_xlim(-20, 20)
ax1.set_ylim(-20, 20)
ax1.set_aspect('equal')

plt.show()