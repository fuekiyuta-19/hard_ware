import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.ticker as ptick
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import glob

from subroutine import font_set, plottool

filepath = "general_python/datalist/20221028/"
dataname = glob.glob(filepath + "*.csv")


datanum = 7
data = pd.read_csv(dataname[datanum])
print(dataname[datanum])

berth = np.full(len(data), -0.24215)

flag = 0
for i in range(len(data)):
    if data['automode'].values[i] == 0:
        flag += 0.1
    else:
        x_ref = data['x_filter'].values[i]
        break

font_set.fig_eekanji()

fig1 = plt.figure(figsize = (10.2, 6.6), dpi = 100, linewidth = 0, edgecolor = 'w')

ax1 = fig1.add_subplot(1, 2, 1)
ax2 = fig1.add_subplot(3, 2, 2)
ax3 = fig1.add_subplot(3, 2, 4)
ax4 = fig1.add_subplot(3, 2, 6)

for j in range(len(data)):
    if j % 10 == 0:
        X, Y = plottool.ship_shape(data['x_filter'].values[j], data['y_filter'].values[j], data['psi_filter'].values[j], 1)
        # X, Y = plottool.ship_shape_dist(data['dist_m_lidar_ma'].values[j], data['psi_raw_rad'].values[j])
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
ax2.set_xlim(0, len(data) / 10)
ax2.set_ylim(-120, 0)
ax2.set_yticks([-100, -80, -60, -40, -20, 0])
ax2.axvline(x = flag, color = 'black')
# ax2.legend(fontsize = 20)

ax3.plot(data['time'].values, data['rudder_right_RC'].values, label = "Without referense speed", color = "r")
# ax3.plot(data['time'].values, data['rudder_right_RC'].values, label = "With referense speed", color = "b")
# ax3.set_ylabel("$\delta_{\mathrm{s}}~ [\mathrm{deg.}]$", fontsize = 31)
ax3.set_ylim(0, 120)
ax3.set_xlim(0, len(data) / 10)
ax3.set_yticks([0, 20, 40, 60, 80, 100])
ax3.axvline(x = flag, color = 'black')
ax3.set_xlim(0, len(data) / 10)

ax4.plot(data['time'].values, data['n_bt_rps_cmd'].values, label = "Without referense speed", color = "r")
# ax4.plot(data['time'].values, data['n_bt_rps_cmd'].values, label = "With referense speed", color = "b")
# ax4.set_ylabel("$n_{\mathrm{bt}}~ [\mathrm{rps}]$", fontsize = 31)
ax4.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
ax4.set_xlim(0, len(data) / 10)
ax4.set_yticks([-30, -15, 0, 15, 30])
ax4.axvline(x = flag, color = 'black')
ax4.set_ylim(-30, 30)

plt.show()

fig2 = plt.figure(figsize = (10.2, 6.6), dpi = 100, linewidth = 0, edgecolor = 'w')
ax1 = fig2.add_subplot(3, 2, 1)
ax2 = fig2.add_subplot(3, 2, 2)
ax3 = fig2.add_subplot(3, 2, 3)
ax4 = fig2.add_subplot(3, 2, 4)
ax5 = fig2.add_subplot(3, 2, 5)
ax6 = fig2.add_subplot(3, 2, 6)

ax1.plot(data['time'].values, data['x_filter'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
ax1.set_ylabel("$X~ [\mathrm{m}]$", fontsize = 20)
ax1.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax1.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
ax1.set_xlim(0, len(data) / 10)
ax1.axvline(x = flag, color = 'black')
ax1.axhline(y = x_ref, color = 'black')
# ax1.set_yticks([ -0.06, -0.03, 0, 0.03])


ax2.plot(data['time'].values, data['u_filter'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
ax2.set_ylabel("$u~ [\mathrm{m/s}]$", fontsize = 20)
ax2.set_xlim(0, len(data) / 10)
ax2.axvline(x = flag, color = 'black')

ax3.plot(data['time'].values, data['y_filter'].values, color = "r")
ax3.plot(data['time'].values, berth, linewidth = 1.0, linestyle = "dashed", label = "$\mathrm{Berth}$", color = "black")
# ax3.plot(data['time'].values, data['dist_m_lidar_ma'].values, color = "blue")
# ax3.plot(data['time'].values, -berth, linewidth = 1.0, linestyle = "dashed", label = "$\mathrm{Berth}$", color = "black")
ax3.set_ylabel("$Y~ [\mathrm{m}]$", fontsize = 20)
ax3.set_xlim(0, len(data) / 10)
# ax3.set_yticks([-1.2, -0.8, -0.4, 0.0])
# ax3.set_ylim(-1.2, 0)
ax3.axvline(x = flag, color = 'black')
# ax3.legend(fontsize = 20)

ax4.plot(data['time'].values, data['velo_ms_lidar_ma'].values, color = "blue")
ax4.plot(data['time'].values, data['vm_filter'].values, color = "r")
ax4.set_ylabel("$v_{m}~ [\mathrm{m/s}]$", fontsize = 20)
ax4.set_xlim(0, len(data) / 10)
ax4.set_ylim(-0.3, 1)
ax4.axhspan(-0.2, 0.011, color = "gray", alpha = 0.2, label = "$\mathrm{Safe~ Speed}$")
ax4.axvline(x = flag, color = 'black')
# ax4.legend(font_size = 20)

ax5.plot(data['time'].values, np.rad2deg(data['psi_filter'].values), label = "Without referense speed", color = "r")
ax5.set_ylabel("$\psi~ [\mathrm{deg.}]$", fontsize = 20)
ax5.set_xlim(0, len(data) / 10)
ax5.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 20)
ax5.axvline(x = flag, color = 'black')
# ax5.legend(fontsize = 17)

ax6.plot(data['time'].values, np.rad2deg(data['r_filter'].values), label = "Without referense speed", color = "r")
ax6.set_ylabel("$r~ [\mathrm{deg./s}]$", fontsize = 20)
ax6.set_xlim(0, len(data) / 10)
ax6.axvline(x = flag, color = 'black')
ax6.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 20)

plt.show()