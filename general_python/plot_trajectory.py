import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.ticker as ptick
import numpy as np

from subroutine import font_set, plottool

filepath = "general_python/datalist/"
dataname = ["TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_38_49",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_42_05",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_45_18",
            "TM_TAKAOKI_NNberthing_time_25-Oct-2022_13_47_37",
            "TAKAOKI_swaytime_26-Oct-2022_16_28_30",
            "TAKAOKI_swaytime_26-Oct-2022_16_33_45",
            "TAKAOKI_swaytime_26-Oct-2022_16_40_11", 
            "TAKAOKI_swaytime_26-Oct-2022_16_42_51",
            "TAKAOKI_swaytime_26-Oct-2022_16_46_44", 
            "TAKAOKI_swaytime_26-Oct-2022_16_47_23",
            "TAKAOKI_swaytime_26-Oct-2022_16_49_18",
            "TAKAOKI_swaytime_26-Oct-2022_17_02_02",
            "TAKAOKI_swaytime_26-Oct-2022_17_05_19",
            "TAKAOKI_swaytime_26-Oct-2022_17_10_19"] 

datanum = 8
data = pd.read_csv(filepath + dataname[datanum] + ".csv")

berth = np.full(len(data), -0.24215)

font_set.fig_eekanji()
fig1 = plt.figure(figsize = (10.2, 6.6), dpi = 100, linewidth = 0, edgecolor = 'w')

ax1 = fig1.add_subplot(1, 2, 1)
ax2 = fig1.add_subplot(3, 2, 2)
ax3 = fig1.add_subplot(3, 2, 4)
ax4 = fig1.add_subplot(3, 2, 6)

for j in range(len(data)):
    if j % 50 == 0:
        # X, Y = plottool.ship_shape(data['y_raw'].values[j], data['x_raw'].values[j], np.rad2deg(data['psi_raw_rad'].values[j]), 1)
        X, Y = plottool.ship_shape_dist(data['dist_m_lidar_ma'].values[j], np.rad2deg(data['psi_raw_rad'].values[j]))
        ax1.plot(X, Y - 10, color = "r", linestyle = "-", lw = 0.5)
    else:
        pass
ax1.plot(plottool.env()[3], plottool.env()[2], color = 'k', linestyle = "-", lw = 0.5)
ax1.plot(plottool.env()[1], plottool.env()[0], color = 'k', linestyle = '-', lw = 0.5)
ax1.fill_between(plottool.env()[3], plottool.env()[2], facecolor = 'k', alpha = 0.3)
ax1.fill_between(plottool.env()[1], plottool.env()[0], facecolor = 'k', alpha = 0.3)
ax1.set_xlim(-5, 5)
ax1.set_ylim(-15, -5)
ax1.set_aspect('equal')

ax2.plot(data['time'].values, data['rudder_left_RC'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
# ax2.plot(data['time'].values, data['rudder_left_RC'].values, label = "$\mathrm{With~ referense~ speed}$", color = "b")
# ax2.set_ylabel("$\delta_{\mathrm{p}~ [\mathrm{deg.}]$", fontsize = 31)
ax2.set_xlim(0, len(data))
ax2.set_ylim(-105, -40)
ax2.set_yticks([-100, -80, -60])
ax2.legend(fontsize = 20)

ax3.plot(data['time'].values, data['rudder_right_RC'].values, label = "Without referense speed", color = "r")
# ax3.plot(data['time'].values, data['rudder_right_RC'].values, label = "With referense speed", color = "b")
# ax3.set_ylabel("$\delta_{\mathrm{s}}~ [\mathrm{deg.}]$", fontsize = 31)
ax3.set_ylim(40, 105)
ax3.set_xlim(0, len(data) / 10)
ax3.set_yticks([60, 80, 100])
ax3.set_xlim(0, len(data) / 10)

ax4.plot(data['time'].values, data['n_bt_rps_cmd'].values, label = "Without referense speed", color = "r")
# ax4.plot(data['time'].values, data['n_bt_rps_cmd'].values, label = "With referense speed", color = "b")
# ax4.set_ylabel("$n_{\mathrm{bt}}~ [\mathrm{rps}]$", fontsize = 31)
ax4.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
ax4.set_xlim(0, len(data) / 10)
ax4.set_yticks([-30, -15, 0, 15, 30])
ax4.set_ylim(-30, 30)

plt.show()

fig2 = pyplot.figure(figsize = (10.2, 6.6), dpi = 100, linewidth = 0, edgecolor = 'w')
ax1 = fig2.add_subplot(3, 2, 1)
ax2 = fig2.add_subplot(3, 2, 2)
ax3 = fig2.add_subplot(3, 2, 3)
ax4 = fig2.add_subplot(3, 2, 4)
ax5 = fig2.add_subplot(3, 2, 5)
ax6 = fig2.add_subplot(3, 2, 6)

ax1.plot(data['time'].values, data['x_raw'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
ax1.set_ylabel("$X~ [\mathrm{m}]$", fontsize = 20)
ax1.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax1.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
ax1.set_xlim(0, len(data) / 10)
ax1.set_yticks([ -0.06, -0.03, 0, 0.03])


ax2.plot(data['time'].values, data['u_dop_raw'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
ax2.set_ylabel("$u~ [\mathrm{m/s}]$", fontsize = 20)
ax2.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax2.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
ax2.set_xlim(0, len(data) / 10)
ax2.set_ylim(-0.005, 0.005)

ax3.plot(data['time'].values, data['y_raw'].values, color = "r")
ax3.set_ylabel("$Y~ [\mathrm{m}]$", fontsize = 20)
ax3.set_xlim(0, len(data) / 10)
ax3.plot(data['time'].values, berth, linewidth = 1.0, linestyle = "dashed", label = "$\mathrm{Berth}$", color = "black")
ax3.set_yticks([-1.2, -0.8, -0.4, 0.0])
ax3.set_ylim(-1.2, 0)
ax3.legend(fontsize = 20)

ax4.plot(data['time'].values, data['dist_m_lidar_ma'].values, color = "r")
ax4.set_ylabel("$v_{m}~ [\mathrm{m/s}]$", fontsize = 20)
ax4.set_xlim(0, len(data) / 10)
ax4.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax4.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
ax4.axhspan(-1, 0.011, color="gray", alpha=0.2, label = "$\mathrm{Safe~ Speed}$")
ax4.legend(fontsize = 20)

ax5.plot(data['time'].values, np.rad2deg(data['psi_raw_rad'].values), label = "Without referense speed", color = "r")
ax5.set_ylabel("$\psi~ [\mathrm{deg.}]$", fontsize = 31)
ax5.set_xlim(0, len(data) / 10)
ax5.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 20)
ax5.legend(fontsize = 17)

ax6.plot(data['time'].values, np.rad2deg(data['r_raw_rad'].values), label = "Without referense speed", color = "r")
ax6.set_ylabel("$r~ [\mathrm{deg./s}]$", fontsize = 31)
ax6.set_xlim(0, len(data) / 10)
ax6.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 20)

plt.show()


