import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import glob
import pandas as pd
from tqdm import tqdm
import animatplot as amp
from subroutine import font_set, plottool, ship_shape
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as ptick

font_set.fig_eekanji()

outputpath = "general_python/datalist/animation/"
filepath   = "general_python/datalist/test/"


dataname1 = ["Result_ref_0_0_15-Sep-2022_16_47_11",
            "Result_ref_270_0.6_15-Sep-2022_20_36_32",
            "Result_ref_270_1.4_15-Sep-2022_20_35_08",
            "Result_ref_90_0.6_15-Sep-2022_17_57_20",
            "Result_ref_90_1.2_15-Sep-2022_17_55_17",
            "Result_ref_180_1_15-Sep-2022_15_56_41",
            "Result_ref_0_1_15-Sep-2022_15_57_42.csv"]
        

dataname2 = ["Result_noref_90_0_15-Sep-2022_15_06_57",
            "Result_noref_270_0.6_15-Sep-2022_20_33_02",
            "Result_noref_270_1.4_15-Sep-2022_20_34_38",
            "Result_noref_90_0.6_15-Sep-2022_17_56_47",
            "Result_noref_90_1.2_15-Sep-2022_17_55_56",
            "Result_noref_180_1_15-Sep-2022_15_57_06",
            "Result_noref_0_1_15-Sep-2022_15_57_24"]


# for k in range(1):
k = 2
data1 = pd.read_csv(filepath + dataname1[k] + ".csv")
data2 = pd.read_csv(filepath + dataname2[k] + ".csv")
length = max(len(data1), len(data2))

heading1 = np.rad2deg(data1['psi'])
heading2 = np.rad2deg(data2['psi'])

rad1 = np.rad2deg(data1['r'])
rad2 = np.rad2deg(data2['r'])

for i in range(len(data1)):
    if heading1[i] >= 180:
        heading1[i] = heading1[i] - 360
    else:
        pass

for i in range(len(data2)):
    if heading2[i] >= 180:
        heading2[i] = heading2[i] - 360
    else:
        pass

fig1 = plt.figure(figsize = (20.4, 8.6), dpi = 200, linewidth = 0, edgecolor = 'w')

ax1  = fig1.add_subplot(1, 4, 1)
ax2  = fig1.add_subplot(3, 4, 2)
ax3  = fig1.add_subplot(3, 4, 6)
ax4  = fig1.add_subplot(3, 4, 10)
ax_x = fig1.add_subplot(3, 4, 3)
ax_u = fig1.add_subplot(3, 4, 4)
ax_y = fig1.add_subplot(3, 4, 7)
ax_v = fig1.add_subplot(3, 4, 8)
ax_p = fig1.add_subplot(3, 4, 11)
ax_r = fig1.add_subplot(3, 4, 12)

def plot_base(data_x, len_lim, flag):

    berth = np.full(len(data_x), -0.24215)

    if flag == 0:
        ref = "$\mathrm{Without~ referense~ speed}$"
        col = "blue"
        ax_v.axhspan(-0.01, 0.011, color = "gray", alpha = 0.2, label = "$\mathrm{Safe~ Speed}$")
        ax_y.plot(data_x['time'].values, berth, linewidth = 1.0, linestyle = "dashed", label = "$\mathrm{Berth}$", color = "black")
        ax_p.plot(data_x['time'].values, heading2, label = ref, color = col)
    else:
        ref = "$\mathrm{With~ referense~ speed}$"
        col = "red"
        ax_p.plot(data_x['time'].values, heading1, label = ref, color = col)
        

        
    ax1.plot(plottool.env()[3], plottool.env()[2], color = 'k', linestyle = "-", lw = 0.5)
    ax1.plot(plottool.env()[1], plottool.env()[0], color = 'k', linestyle = '-', lw = 0.5)
    ax1.fill_between(plottool.env()[3], plottool.env()[2], facecolor = 'k', alpha = 0.3)
    ax1.fill_between(plottool.env()[1], plottool.env()[0], facecolor = 'k', alpha = 0.3)
    ax1.set_xlim(-3, 1.1)
    ax1.set_yticks([-50, 50])
    ax1.set_ylim(-9.5, -1)
    ax1.set_xlabel("$Y~ [\mathrm{m}]$", fontsize = 31)
    ax1.text(-2.6, -1.8, "$1.4~ [\mathrm{m/s}]$", fontsize = 22)
    ax1.quiver(-2.55, -2.0, 1.0, 0, color = "black",
            angles = 'xy', scale_units = 'xy', scale = 1, width = 0.012)

    ax2.set_ylabel("$\delta_{\mathrm{p}}~ [\mathrm{deg.}]$", fontsize = 25)
    ax2.plot(data_x['time'].values, data_x['left_rudder'].values, label = ref, color = col)
    ax2.set_xlim(0, len_lim/10)
    ax2.set_ylim(-100, -60)
    ax2.set_yticks([-100, -80, -60])
    ax2.legend(fontsize = 13, loc = 'upper right')

    ax3.set_ylabel("$\delta_{\mathrm{s}}~ [\mathrm{deg.}]$", fontsize = 25)
    ax3.plot(data_x['time'].values, data_x['right_rudder'].values, label = ref, color = col)
    ax3.set_ylim(60, 100)
    ax3.set_yticks([60, 80, 100])
    ax3.set_xlim(0, len_lim/10)

    ax4.set_ylabel("$n_{\mathrm{bt}}~ [\mathrm{rps}]$", fontsize = 25)
    ax4.plot(data_x['time'].values, data_x['bow_rps'].values, label = ref, color = col)
    ax4.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 25)
    ax4.set_xlim(0, len_lim/10)
    ax4.set_yticks([-30, -15, 0, 15, 30])
    ax4.set_ylim(-30, 30)

    ax_x.set_ylabel("$X~ [\mathrm{m}]$", fontsize = 25)
    ax_x.plot(data_x['time'].values, data_x['X'].values, label = ref, color = col)
    # ax_x.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
    ax_x.set_xlim(0, len_lim/10)
    # ax_x.set_yticks([-30, -15, 0, 15, 30])
    # ax_x.set_ylim(-30, 30)

    ax_u.set_ylabel("$u~ [\mathrm{m/s}]$", fontsize = 25)
    ax_u.plot(data_x['time'].values, data_x['u'].values, label = ref, color = col)
    # ax_u.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
    ax_u.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
    ax_u.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
    ax_u.set_xlim(0, len_lim/10)
    # ax_u.set_ylim(-0.004, 0.0041)
    ax_u.set_ylim(-0.001, 0.011)

    ax_y.set_ylabel("$Y~ [\mathrm{m}]$", fontsize = 25)
    ax_y.plot(data_x['time'].values, data_x['Y'].values, color = col)
    # ax_y.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
    ax_y.legend(fontsize = 13, loc = 'lower right')
    ax_y.set_ylim(-1.2, 0.01)
    ax_y.set_xlim(0, len_lim/10)

    ax_v.set_ylabel("$v_{m}~ [\mathrm{m/s}]$", fontsize = 25)
    ax_v.plot(data_x['time'].values, data_x['vm'].values, color = col)
    # ax_v.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
    ax_v.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
    ax_v.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
    ax_v.set_xlim(0, len_lim/10)
    ax_v.set_ylim(-0.0001, 0.041)
    ax_v.legend(fontsize = 13, loc = 'upper right')

    ax_p.set_ylabel("$\psi~ [\mathrm{deg.}]$", fontsize = 25)
    # ax_p.plot(data_x['time'].values, data_x['psi'].values, label = ref, color = col)
    ax_p.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 25)
    ax_p.set_xlim(0, len_lim/10)
    # ax_p.legend(fontsize = 13, loc = 'upper right')

    ax_r.set_ylabel("$r~ [\mathrm{deg./s}]$", fontsize = 25)
    ax_r.plot(data_x['time'].values, np.rad2deg(data_x['r'].values), label = ref, color = col)
    ax_r.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 25)
    ax_r.set_xlim(0, len_lim/10)    
    ax_r.set_ylim(-1, 1)    

    plt.tight_layout()   

def plot_data_line(ax_k, df_x, df_y, col, t):

    ax_k.plot(df_x[t], df_y[t], marker = 'o', color =col , zorder = 10)
    ax_k.axvline(x = df_x[t], color = col, lw = 0.3)

def update(t):

    if t % 5 != 0:
        print(t)

    else:

        ax1.cla() 
        ax2.cla() 
        ax3.cla() 
        ax4.cla() 
        ax_x.cla()
        ax_u.cla()
        ax_y.cla()
        ax_v.cla()
        ax_p.cla()
        ax_r.cla()
        print(t + 1, " / ", length)

        if t >= len(data1):
            plot_base(data1, length, 1)
            X, Y = plottool.ship_shape(data1['X'].values[len(data1) - 1], data1['Y'].values[len(data1) - 1], data1['psi'].values[len(data1) - 1], 1)
            ax1.plot(Y, X-3, color = "red", linestyle = "-", lw = 0.5)
            plot_data_line(ax2,  data1['time'].values, data1['left_rudder'].values, "red", len(data1) - 1)
            plot_data_line(ax3,  data1['time'].values, data1['right_rudder'].values, "red", len(data1) - 1)
            plot_data_line(ax4,  data1['time'].values, data1['bow_rps'].values, "red", len(data1) - 1)
            plot_data_line(ax_x, data1['time'].values, data1['X'].values, "red", len(data1) - 1)
            plot_data_line(ax_u, data1['time'].values, data1['u'].values, "red", len(data1) - 1)
            plot_data_line(ax_y, data1['time'].values, data1['Y'].values, "red", len(data1) - 1)
            plot_data_line(ax_v, data1['time'].values, data1['vm'].values, "red", len(data1) - 1)
            plot_data_line(ax_p, data1['time'].values, heading1, "red", len(data1) - 1)
            plot_data_line(ax_r, data1['time'].values, np.rad2deg(data1['r'].values), "red", len(data1) - 1)

        else:
            plot_base(data1, length, 1)
            X, Y = plottool.ship_shape(data1['X'].values[t], data1['Y'].values[t], data1['psi'].values[t], 1)
            ax1.plot(Y, X-3, color = "red", linestyle = "-", lw = 0.5)
            plot_data_line(ax2,  data1['time'].values, data1['left_rudder'].values, "red", t)
            plot_data_line(ax3,  data1['time'].values, data1['right_rudder'].values, "red", t)
            plot_data_line(ax4,  data1['time'].values, data1['bow_rps'].values, "red", t)
            plot_data_line(ax_x, data1['time'].values, data1['X'].values, "red", t)
            plot_data_line(ax_u, data1['time'].values, data1['u'].values, "red", t)
            plot_data_line(ax_y, data1['time'].values, data1['Y'].values, "red", t)
            plot_data_line(ax_v, data1['time'].values, data1['vm'].values, "red", t)
            plot_data_line(ax_p, data1['time'].values, heading1, "red", t)
            plot_data_line(ax_r, data1['time'].values, np.rad2deg(data1['r'].values), "red", t)

        if t >= len(data2):
            plot_base(data2, length, 0)
            X, Y = plottool.ship_shape(data2['X'].values[len(data2) - 1], data2['Y'].values[len(data2) - 1], data2['psi'].values[len(data2) - 1], 1)
            ax1.plot(Y, X-7, color = "blue", linestyle = "-", lw = 0.5)
            plot_data_line(ax2,  data2['time'].values, data2['left_rudder'].values, "blue", len(data2) - 1)
            plot_data_line(ax3,  data2['time'].values, data2['right_rudder'].values, "blue", len(data2) - 1)
            plot_data_line(ax4,  data2['time'].values, data2['bow_rps'].values, "blue", len(data2) - 1)
            plot_data_line(ax_x, data2['time'].values, data2['X'].values, "blue", len(data2) - 1)
            plot_data_line(ax_u, data2['time'].values, data2['u'].values, "blue", len(data2) - 1)
            plot_data_line(ax_y, data2['time'].values, data2['Y'].values, "blue", len(data2) - 1)
            plot_data_line(ax_v, data2['time'].values, data2['vm'].values, "blue", len(data2) - 1)
            plot_data_line(ax_p, data2['time'].values, heading2, "blue", len(data2) - 1)
            plot_data_line(ax_r, data2['time'].values, np.rad2deg(data2['r'].values), "blue", len(data2) - 1)
        
        else:
            plot_base(data2, length, 0)
            X, Y = plottool.ship_shape(data2['X'].values[t], data2['Y'].values[t], data2['psi'].values[t], 1)
            ax1.plot(Y, X-7, color = "blue", linestyle = "-", lw = 0.5)
            plot_data_line(ax2,  data2['time'].values, data2['left_rudder'].values, "blue", t)
            plot_data_line(ax3,  data2['time'].values, data2['right_rudder'].values, "blue", t)
            plot_data_line(ax4,  data2['time'].values, data2['bow_rps'].values, "blue", t)
            plot_data_line(ax_x, data2['time'].values, data2['X'].values, "blue", t)
            plot_data_line(ax_u, data2['time'].values, data2['u'].values, "blue", t)
            plot_data_line(ax_y, data2['time'].values, data2['Y'].values, "blue", t)
            plot_data_line(ax_v, data2['time'].values, data2['vm'].values, "blue", t)
            plot_data_line(ax_p, data2['time'].values, heading2, "red", t)
            plot_data_line(ax_r, data2['time'].values, np.rad2deg(data2['r'].values), "blue", t)

anim = FuncAnimation(fig1, update, length, interval=30)

anim.save(outputpath + dataname1[k] + '.mp4', writer="ffmpeg")

print("Task Finish")
