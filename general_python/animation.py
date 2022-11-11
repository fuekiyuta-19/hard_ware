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
            

for k in range(3):
    data1 = pd.read_csv(filepath + dataname1[k]+ ".csv")
    data2 = pd.read_csv(filepath + dataname2[k] + ".csv")
    length = max(len(data1), len(data2))

    fig1 = plt.figure(figsize = (20.4, 6.6), dpi = 200, linewidth = 0, edgecolor = 'w')

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

    def plot(data_x, len_lim, flag):
        if flag == 0:
            ref = "$\mathrm{Without~ referense~ speed}$"
            col = "red"
        else:
            ref = "$\mathrm{With~ referense~ speed}$"
            col = "blue"

        ax1.plot(plottool.env()[3], plottool.env()[2], color = 'k', linestyle = "-", lw = 0.5)
        ax1.plot(plottool.env()[1], plottool.env()[0], color = 'k', linestyle = '-', lw = 0.5)
        ax1.fill_between(plottool.env()[3], plottool.env()[2], facecolor = 'k', alpha = 0.3)
        ax1.fill_between(plottool.env()[1], plottool.env()[0], facecolor = 'k', alpha = 0.3)
        ax1.set_xlim(-3, 1.1)
        ax1.set_yticks([-50, 50])
        ax1.set_ylim(-9.5, -1)
        ax1.set_xlabel("$Y~ [\mathrm{m}]$", fontsize = 31)
        ax1.text(-2.6, 2.9, "$0.6~ [\mathrm{m/s}]$", fontsize = 22)
        ax1.quiver(-1.7, 3.2, -1.0, 0, color = "black",
                angles = 'xy', scale_units = 'xy', scale = 1, label = "Wind", width = 0.012)

        ax2.set_ylabel("$\delta_{\mathrm{p}}~ [\mathrm{deg.}]$", fontsize = 31)
        ax2.plot(data_x['time'].values, data_x['left_rudder'].values, label = ref, color = col)
        ax2.set_xlim(0, len_lim/10)
        ax2.set_ylim(-100, -60)
        ax2.set_yticks([-100, -80, -60])
        ax2.legend(fontsize = 13, loc = 'upper right')

        ax3.set_ylabel("$\delta_{\mathrm{s}}~ [\mathrm{deg.}]$", fontsize = 31)
        ax3.plot(data_x['time'].values, data_x['right_rudder'].values, label = ref, color = col)
        ax3.set_ylim(60, 100)
        ax3.set_yticks([60, 80, 100])
        ax3.set_xlim(0, len_lim/10)

        ax4.set_ylabel("$n_{\mathrm{bt}}~ [\mathrm{rps}]$", fontsize = 31)
        ax4.plot(data_x['time'].values, data_x['bow_rps'].values, label = ref, color = col)
        # ax4.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax4.set_xlim(0, len_lim/10)
        ax4.set_yticks([-30, -15, 0, 15, 30])
        ax4.set_ylim(-30, 30)

        ax_x.set_ylabel("$X~ [\mathrm{m}]$", fontsize = 31)
        ax_x.plot(data_x['time'].values, data_x['X'].values, label = ref, color = col)
        # ax_x.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_x.set_xlim(0, len_lim/10)
        # ax_x.set_yticks([-30, -15, 0, 15, 30])
        # ax_x.set_ylim(-30, 30)

        ax_u.set_ylabel("$u~ [\mathrm{m/s}]$", fontsize = 31)
        ax_u.plot(data_x['time'].values, data_x['u'].values, label = ref, color = col)
        ax_u.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_u.set_xlim(0, len_lim/10)

        ax_y.set_ylabel("$Y~ [\mathrm{m}]$", fontsize = 31)
        ax_y.plot(data_x['time'].values, data_x['Y'].values, label = ref, color = col)
        # ax_y.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_y.set_xlim(0, len_lim/10)

        ax_v.set_ylabel("$v_{m}~ [\mathrm{m/s}]$", fontsize = 31)
        ax_v.plot(data_x['time'].values, data_x['vm'].values, label = ref, color = col)
        # ax_v.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_v.axhspan(-0.2, 0.011, color = "gray", alpha = 0.2, label = "$\mathrm{Safe~ Speed}$")
        ax_v.set_xlim(0, len_lim/10)
        ax_v.legend(fontsize = 13, loc = 'lower right')

        ax_p.set_ylabel("$\psi~ [\mathrm{deg.}]$", fontsize = 31)
        ax_p.plot(data_x['time'].values, data_x['psi'].values, label = ref, color = col)
        ax_p.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_p.set_xlim(0, len_lim/10)
        ax_p.legend(fontsize = 13, loc = 'upper right')

        ax_r.set_ylabel("$r~ [\mathrm{deg./s}]$", fontsize = 31)
        ax_r.plot(data_x['time'].values, np.rad2deg(data_x['r'].values), label = ref, color = col)
        ax_r.set_xlabel("$t~ [\mathrm{s}]$", fontsize = 31)
        ax_r.set_xlim(0, len_lim/10)

    ims = []                     

    def update(t):

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
            plot(data1, length, 1)
            X, Y = plottool.ship_shape(data1['X'].values[len(data1) - 1], data1['Y'].values[len(data1) - 1], data1['psi'].values[len(data1) - 1], 1)
            ax1.plot(Y, X-3, color = "red", linestyle = "-", lw = 0.5)
            ax2.plot(data1['time'].values[len(data1) - 1], data1['left_rudder'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax2.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax3.plot(data1['time'].values[len(data1) - 1], data1['right_rudder'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax3.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax4.plot(data1['time'].values[len(data1) - 1], data1['bow_rps'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax4.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_x.plot(data1['time'].values[len(data1) - 1], data1['X'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax_x.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_u.plot(data1['time'].values[len(data1) - 1], data1['u'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax_u.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_y.plot(data1['time'].values[len(data1) - 1], data1['Y'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax_y.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_v.plot(data1['time'].values[len(data1) - 1], data1['vm'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax_v.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_p.plot(data1['time'].values[len(data1) - 1], data1['psi'].values[len(data1) - 1], marker = 'o', color = "r", zorder = 10)
            ax_p.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)
            ax_r.plot(data1['time'].values[len(data1) - 1], np.rad2deg(data1['r'].values[len(data1) - 1]), marker = 'o', color = "r", zorder = 10)
            ax_r.axvline(x = data1['time'].values[len(data1) - 1], color = 'red', lw = 0.3)

        else:

            plot(data1, length, 1)
            X, Y = plottool.ship_shape(data1['X'].values[t], data1['Y'].values[t], data1['psi'].values[t], 1)
            ax1.plot(Y, X-3, color = "red", linestyle = "-", lw = 0.5)
            ax2.plot(data1['time'].values[t], data1['left_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
            ax2.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax3.plot(data1['time'].values[t], data1['right_rudder'].values[t], marker = 'o', color = "r", zorder = 10)
            ax3.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax4.plot(data1['time'].values[t], data1['bow_rps'].values[t], marker = 'o', color = "r", zorder = 10)
            ax4.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_x.plot(data1['time'].values[t], data1['X'].values[t], marker = 'o', color = "r", zorder = 10)
            ax_x.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_u.plot(data1['time'].values[t], data1['u'].values[t], marker = 'o', color = "r", zorder = 10)
            ax_u.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_y.plot(data1['time'].values[t], data1['Y'].values[t], marker = 'o', color = "r", zorder = 10)
            ax_y.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_v.plot(data1['time'].values[t], data1['vm'].values[t], marker = 'o', color = "r", zorder = 10)
            ax_v.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_p.plot(data1['time'].values[t], data1['psi'].values[t], marker = 'o', color = "r", zorder = 10)
            ax_p.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)
            ax_r.plot(data1['time'].values[t], np.rad2deg(data1['r'].values[t]), marker = 'o', color = "r", zorder = 10)
            ax_r.axvline(x = data1['time'].values[t], color = 'red', lw = 0.3)



        if t >= len(data2):
            plot(data2, length, 0)
            X, Y = plottool.ship_shape(data2['X'].values[len(data2) - 1], data2['Y'].values[len(data2) - 1], data2['psi'].values[len(data2) - 1], 1)
            ax1.plot(Y, X-7, color = "blue", linestyle = "-", lw = 0.5)
            ax2.plot(data2['time'].values[len(data2) - 1], data2['left_rudder'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax2.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax3.plot(data2['time'].values[len(data2) - 1], data2['right_rudder'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax3.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax4.plot(data2['time'].values[len(data2) - 1], data2['bow_rps'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax4.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_x.plot(data2['time'].values[len(data2) - 1], data2['X'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax_x.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_u.plot(data2['time'].values[len(data2) - 1], data2['u'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax_u.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_y.plot(data2['time'].values[len(data2) - 1], data2['Y'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax_y.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_v.plot(data2['time'].values[len(data2) - 1], data2['vm'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax_v.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_p.plot(data2['time'].values[len(data2) - 1], data2['psi'].values[len(data2) - 1], marker = 'o', color = "blue", zorder = 10)
            ax_p.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
            ax_r.plot(data2['time'].values[len(data2) - 1], np.rad2deg(data2['r'].values[len(data2) - 1]), marker = 'o', color = "blue", zorder = 10)
            ax_r.axvline(x = data2['time'].values[len(data2) - 1], color = 'blue', lw = 0.3)
        
        else:

            plot(data2, length, 0)
            X, Y = plottool.ship_shape(data2['X'].values[t], data2['Y'].values[t], data2['psi'].values[t], 1)
            ax1.plot(Y, X-7, color = "blue", linestyle = "-", lw = 0.5)
            ax2.plot(data2['time'].values[t], data2['left_rudder'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax2.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax3.plot(data2['time'].values[t], data2['right_rudder'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax3.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax4.plot(data2['time'].values[t], data2['bow_rps'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax4.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_x.plot(data2['time'].values[t], data2['X'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax_x.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_u.plot(data2['time'].values[t], data2['u'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax_u.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_y.plot(data2['time'].values[t], data2['Y'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax_y.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_v.plot(data2['time'].values[t], data2['vm'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax_v.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_p.plot(data2['time'].values[t], data2['psi'].values[t], marker = 'o', color = "blue", zorder = 10)
            ax_p.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)
            ax_r.plot(data2['time'].values[t], np.rad2deg(data2['r'].values[t]), marker = 'o', color = "blue", zorder = 10)
            ax_r.axvline(x = data2['time'].values[t], color = 'blue', lw = 0.3)


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

    anim = FuncAnimation(fig1, update, range(length), interval=30)
    # anim.show()

    anim.save(outputpath + dataname1[k] + '.mp4', writer="ffmpeg")

print("Task Finish")

# ani = animation.ArtistAnimation(fig1, ims)

# ani.save(outputpath + dataname1[0] + '.mp4', writer='ffmpeg', fps = 100)

# rc('animation', html='jshtml')
# print("Task Finish")