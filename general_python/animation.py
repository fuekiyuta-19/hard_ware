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


font_set.fig_eekanji()

outputpath = "general_python/datalist/animation/"
filepath   = "general_python/datalist/test/"


dataname1 = ["Result_ref_0_0_15-Sep-2022_16_47_11",
            "Result_ref_90_0.6_15-Sep-2022_17_57_20",
            "Result_ref_90_1.2_15-Sep-2022_17_55_17",
            "Result_ref_180_1_15-Sep-2022_15_56_41",
            "Result_ref_0_1_15-Sep-2022_15_57_42.csv",
            "Result_ref_270_0.6_15-Sep-2022_20_36_32",
            "Result_ref_270_1.4_15-Sep-2022_20_35_08"]


dataname2 = ["Result_noref_90_0_15-Sep-2022_15_06_57",
            "Result_noref_90_0.6_15-Sep-2022_17_56_47",
            "Result_noref_90_1.2_15-Sep-2022_17_55_56",
            "Result_noref_180_1_15-Sep-2022_15_57_06",
            "Result_noref_0_1_15-Sep-2022_15_57_24",
            "Result_noref_270_0.6_15-Sep-2022_20_33_02",
            "Result_noref_270_1.4_15-Sep-2022_20_34_38"]


data1 = pd.read_csv(filepath + dataname1[0]+ ".csv")
data2 = pd.read_csv(filepath + dataname2[0] + ".csv")
length = max(len(data1), len(data2))

fig1 = plt.figure(figsize = (15.2, 9.6), dpi = 200, linewidth = 0, edgecolor = 'w')

ax1 = fig1.add_subplot(1, 2, 1)
ax2 = fig1.add_subplot(3, 2, 2)
ax3 = fig1.add_subplot(3, 2, 4)
ax4 = fig1.add_subplot(3, 2, 6)

def plot(data_x, len_lim):
    ax1.plot(plottool.env()[3], plottool.env()[2], color = 'k', linestyle = "-", lw = 0.5)
    ax1.plot(plottool.env()[1], plottool.env()[0], color = 'k', linestyle = '-', lw = 0.5)
    ax1.fill_between(plottool.env()[3], plottool.env()[2], facecolor = 'k', alpha = 0.3)
    ax1.fill_between(plottool.env()[1], plottool.env()[0], facecolor = 'k', alpha = 0.3)
    ax1.set_xlim(-3, 1.1)
    ax1.set_yticks([-50, 50])
    ax1.set_ylim(-1, -12)
    ax1.set_xlabel("$Y~ [\mathrm{m}]$", fontsize = 31)
    ax1.text(-2.6, 2.9, "$0.6~ [\mathrm{m/s}]$", fontsize = 22)
    ax1.quiver(-1.7, 3.2, -1.0, 0, color = "black",
            angles = 'xy', scale_units = 'xy', scale = 1, label = "Wind", width = 0.012)

    ax2.set_ylabel("$\delta_{\mathrm{p}}~ [\mathrm{deg.}]$", fontsize = 31)
    ax2.plot(data_x['time'].values, data_x['left_rudder'].values, label = "$\mathrm{Without~ referense~ speed}$", color = "r")
    ax2.set_xlim(0, len_lim/10)
    ax2.set_ylim(-100, -60)
    ax2.set_yticks([-100, -80, -60])
    ax2.legend(fontsize = 20)

    ax3.set_ylabel("$\delta_{\mathrm{s}}~ [\mathrm{deg.}]$", fontsize = 31)
    ax3.plot(data_x['time'].values, data_x['right_rudder'].values, label = "Without referense speed", color = "r")
    ax3.set_ylim(60, 100)
    ax3.set_yticks([60, 80, 100])
    ax3.set_xlim(0, len_lim/10)

    ax4.set_ylabel("$n_{\mathrm{bt}}~ [\mathrm{rps}]$", fontsize = 31)
    ax4.plot(data_x['time'].values, data_x['bow_rps'].values, label = "Without referense speed", color = "r")
    ax4.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
    ax4.set_xlim(0, len_lim/10)
    ax4.set_yticks([-30, -15, 0, 15, 30])
    ax4.set_ylim(-30, 30)

ims = []                     

def update(t):

    ax1.cla() 
    ax2.cla() 
    ax3.cla() 
    ax4.cla() 
    if t >= len(data1):
        plot(data1, length)
        X, Y = plottool.ship_shape(data1['X'].values[len(data1) - 1], data1['Y'].values[len(data1) - 1], data1['psi'].values[len(data1) - 1], 1)
        ax1.plot(Y, X-10, color = "r", linestyle = "-", lw = 0.5)
        ax2.plot(data1['time'].values[len(data1)], data1['left_rudder'].values[len(data1)], marker = 'o', color = "r", zorder = 10)
        ax2.axvline(x = data1['time'].values[len(data1)], color = 'red', lw = 0.3)
        ax3.plot(data1['time'].values[len(data1)], data1['right_rudder'].values[len(data1)], marker = 'o', color = "r", zorder = 10)
        ax3.axvline(x = data1['time'].values[len(data1)], color = 'red', lw = 0.3)
        ax4.plot(data1['time'].values[len(data1)], data1['bow_rps'].values[len(data1)], marker = 'o', color = "r", zorder = 10)
        ax4.axvline(x = data1['time'].values[len(data1)], color = 'red', lw = 0.3)
    else:

        plot(data1, length)
        X, Y = plottool.ship_shape(data1['X'].values[t], data1['Y'].values[t], data1['psi'].values[t], 1)
        ax1.plot(Y, X-10, color = "r", linestyle = "-", lw = 0.5)
        ax2.plot(data1['time'].values[t], data1['left_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
        ax2.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
        ax3.plot(data1['time'].values[t], data1['right_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
        ax3.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
        ax4.plot(data1['time'].values[t], data1['bow_rps'].values[t], marker = 'o', color = "r", zorder = 10)
        ax4.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)

    if t >= len(data2):
        plot(data2, length)
        X, Y = plottool.ship_shape(data2['X'].values[len(data2) - 1], data2['Y'].values[len(data2) - 1], data2['psi'].values[len(data2) - 1], 1)
        ax1.plot(Y, X-10, color = "r", linestyle = "-", lw = 0.5)
        ax2.plot(data2['time'].values[len(data2)], data2['left_rudder'].values[len(data2)], marker = 'o', color = "r", zorder = 10)
        ax2.axvline(x = data2['time'].values[len(data2)], color = 'red', lw = 0.3)
        ax3.plot(data2['time'].values[len(data2)], data2['right_rudder'].values[len(data2)], marker = 'o', color = "r", zorder = 10)
        ax3.axvline(x = data2['time'].values[len(data2)], color = 'red', lw = 0.3)
        ax4.plot(data2['time'].values[len(data2)], data2['bow_rps'].values[len(data2)], marker = 'o', color = "r", zorder = 10)
        ax4.axvline(x = data2['time'].values[len(data2)], color = 'red', lw = 0.3)
    
    else:

        plot(data2, length)
        X, Y = plottool.ship_shape(data2['X'].values[t], data2['Y'].values[t], data2['psi'].values[t], 1)
        ax1.plot(Y, X-10, color = "r", linestyle = "-", lw = 0.5)
        ax2.plot(data2['time'].values[t], data2['left_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
        ax2.axvline(x = data2['time'].values[t], color = 'red', lw = 0.3)
        ax3.plot(data2['time'].values[t], data2['right_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
        ax3.axvline(x = data2['time'].values[t], color = 'red', lw = 0.3)
        ax4.plot(data2['time'].values[t], data2['bow_rps'].values[t], marker = 'o', color = "r", zorder = 10)
        ax4.axvline(x = data2['time'].values[t], color = 'red', lw = 0.3)


# for t in range(len(data1)):
#     print(t + 1, " / ", len(data1))
#     time = t / 10                            
#     X, Y = plottool.ship_shape(data1['X'].values[t], data1['Y'].values[t], data1['psi'].values[t], 1)
#     im1  = ax1.plot(Y, X, color = "r", linestyle = "-", lw = 0.5)
#     # im2  = ax2.plot(data['time'].values[t], data['rudder_left_cmd'].values[t], label = "$\mathrm{Without~ referense~ speed}$", color = "r")
#     # im3  = ax3.plot(data['time'].values[t], data['rudder_right_cmd'].values[t], label = "Without referense speed", color = "r")
#     # im4  = ax4.plot(data['time'].values[t], data['n_bt_rps_cmd'].values[t], label = "Without referense speed", color = "r")
    
#     im2  = ax2.plot(data1['time'].values[t], data1['left_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
#     im5  = ax2.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
#     im5  = amp.blocks.Line(X_d, Y_d, ax=ax2)
#     im3  = ax3.plot(data1['time'].values[t], data1['right_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
#     im6  = amp.blocks.Line(X_d, Y_d, ax=ax3)
#     im4  = ax4.plot(data1['time'].values[t], data1['bow_rps'].values[t], marker = 'o', color = "r", zorder = 10)
#     im7  = amp.blocks.Line(X_d, Y_d, ax=ax4)

#     # title = ax.text(150, 120, 'Time='+str(time)+'s')
    
#     ims.append(im1 + im2 + im3 + im4 + im5 + im6 + im7)

anim = FuncAnimation(fig1, update, range(length), interval=150)

anim.save(outputpath + dataname1[0] + '.mp4', writer="ffmpeg")
print("Task Finish")
# ani = animation.ArtistAnimation(fig1, ims)

# ani.save(outputpath + dataname1[0] + '.mp4', writer='ffmpeg', fps = 100)

# rc('animation', html='jshtml')
# print("Task Finish")