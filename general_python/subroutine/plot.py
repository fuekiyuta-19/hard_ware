
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from utils.font import font_setting
from utils.ship_shape import ship_coo, rudder_s_coo, rudder_p_coo

k = 9
FIG_SIZE = (1.6*k, 1*k)
DPI = 350

Lpp = 150
B = 24.3


def plot(result_csv, berth_csv, output_name):
    # Load Result
    df = pd.read_csv(result_csv).reset_index()
    
    # rad -> deg.
    df['psi [rad]']  = df['psi [rad]'].apply(lambda x: np.rad2deg(x))
    df['r [rad/s]']    = df['r [rad/s]'].apply(lambda x: np.rad2deg(x))
    df['delta_p_r [rad]'] = df['delta_p_r [rad]'].apply(lambda x: np.rad2deg(x))
    df['delta_s_r [rad]'] = df['delta_s_r [rad]'].apply(lambda x: np.rad2deg(x))

    # Load Berth
    berth_df = pd.read_csv(berth_csv)

    # Define Fig
    font_setting()
    fig = plt.figure(figsize=FIG_SIZE, dpi=DPI)
    gs_master = GridSpec(nrows=4, ncols=4, height_ratios=[1, 1, 1, 1])
    #
    gs_1 = GridSpecFromSubplotSpec(
        nrows=3, ncols=2, subplot_spec=gs_master[0:3, 0:2])
    axes_1 = fig.add_subplot(gs_1[:, :])
    #
    gs_234 = GridSpecFromSubplotSpec(
        nrows=3, ncols=1, subplot_spec=gs_master[0:3, 2])
    axes_2 = fig.add_subplot(gs_234[0, :])
    axes_3 = fig.add_subplot(gs_234[1, :])
    axes_4 = fig.add_subplot(gs_234[2, :])
    #
    gs_567 = GridSpecFromSubplotSpec(
        nrows=3, ncols=1, subplot_spec=gs_master[0:3, 3])
    axes_5 = fig.add_subplot(gs_567[0, :])
    axes_6 = fig.add_subplot(gs_567[1, :])
    axes_7 = fig.add_subplot(gs_567[2, :])
    #
    gs_8901 = GridSpecFromSubplotSpec(
        nrows=1, ncols=4, subplot_spec=gs_master[3, :])
    axes_8 = fig.add_subplot(gs_8901[:, 0])
    axes_9 = fig.add_subplot(gs_8901[:, 1])
    axes_10 = fig.add_subplot(gs_8901[:, 2])
    axes_11 = fig.add_subplot(gs_8901[:, 3])

    #
    colors = ["Black"]
    #
    trajectory_plot(axes_1, df, berth_df, colors)
    #
    xlabel = "$t \ \mathrm{[s]}$"
    colors = ["black"]
    #
    columns = ["x [m]"]
    ylabel = "$x_{0} \ \mathrm{[m]}$"
    pos_plot(axes_2, df, columns, colors,
             xlabel=xlabel, ylabel=ylabel)
    columns = ["y [m]", ]
    ylabel = "$y_{0} \ \mathrm{[m]}$"
    pos_plot(axes_3, df, columns, colors,
             xlabel=xlabel, ylabel=ylabel)
    columns = ["psi [rad]"]
    ylabel = "$\psi \ \mathrm{[deg.]}$"
    pos_plot(axes_4, df, columns, colors,
             xlabel=xlabel, ylabel=ylabel)
    #
    columns = ["u [m/s]"]
    ylabel = "$u \ \mathrm{[kts]}$"
    velo_plot(axes_5, df, columns, colors,
              xlabel=xlabel, ylabel=ylabel)
    columns = ["vm [m/s]"]
    ylabel = "$v_{m} \ \mathrm{[kts]}$"
    velo_plot(axes_6, df, columns, colors,
              xlabel=xlabel, ylabel=ylabel)
    columns = ["r [rad/s]"]
    ylabel = "$r \ \mathrm{[deg./s]}$"
    velo_plot(axes_7, df, columns, colors,
              xlabel=xlabel, ylabel=ylabel)
    #
    colors = ["black", "red"]
    legends = ['command', 'real']
    #
    columns = ['delta_p_r [rad]']
    ylabel = "$\delta_{\mathrm{p}} \ \mathrm{[deg.]}$"
    control_plot(axes_8, df, columns, colors, legends,
                 xlabel=xlabel, ylabel=ylabel, legend_flag=True)
    columns = ['delta_s_r [rad]']
    ylabel = "$\delta_{\mathrm{s}} \ \mathrm{[deg.]}$"
    control_plot(axes_9, df, columns, colors, legends,
                 xlabel=xlabel, ylabel=ylabel)
    columns = ['np [rps]']
    ylabel = "$n \ \mathrm{[rps]}$"
    control_plot_2(axes_10, df, columns, colors, legends,
                 xlabel=xlabel, ylabel=ylabel)
    columns = ['ThrusterCurrent [mA]']
    ylabel = "$i_{\mathrm{BT}} \ \mathrm{[mA]}$"
    control_plot_2(axes_11, df, columns, colors, legends,
                 xlabel=xlabel, ylabel=ylabel)
    #
    fig.tight_layout()
    fig.savefig(f'fig/{output_name}.pdf')
    # plt.show()


def trajectory_plot(ax, df, berth_df, colors):
    # setting
    ax.set_xlabel('$y_0 \ \mathrm{[m]}$')
    ax.set_ylabel('$x_0 \ \mathrm{[m]}$')
    ax.set_aspect('equal')

    # obstacle
    if berth_df.isnull().values.sum() >= 1:
        berth_num_list = list(berth_df[berth_df["X"].isnull()].index.values)
        berth_num_list.append(len(berth_df))

        for i in range(len(berth_num_list)-1):
            berth_df_1 = berth_df[berth_num_list[i]+1 : berth_num_list[i+1]-1]
            berth_array = berth_df_1.values
            pos = []
            for j in range(len(berth_array)-1):
                pos.append(berth_array[j, [0,1]])
            berth_poly = plt.Polygon(
                pos,
                fill=True,
                alpha=1.0,
                linewidth=0.3,
                fc="#C8CCDE",
                ec="#0A0F60"
            )
            berth = ax.add_patch(berth_poly)
    else:
        berth_array = berth_df.values
        pos = []
        for i in range(len(berth_array)-1):
            pos.append(berth_array[i, [0,1]])
        berth_poly = plt.Polygon(
            pos,
            fill=True,
            alpha=1.0,
            linewidth=0.3,
            fc="#C8CCDE",
            ec="#0A0F60"
        )
        berth = ax.add_patch(berth_poly)

    # ship shape
    for step in range(0, len(df), 150):
        x = df[[
            'x [m]', 'u [m/s]',
            'y [m]', 'vm [m/s]',
            'psi [rad]', 'r [rad/s]'
        ]].to_numpy()[step, :]

        u = df[[
            'np [rps]', 'delta_p_r [rad]', 'delta_s_r [rad]',
            'ThrusterCurrent [mA]'
        ]].to_numpy()[step, :]

        ship_poly = plt.Polygon(
            ship_coo(x, Lpp, B)[:, [1,0]],
            fill=False,
            alpha=0.8,
            linewidth=0.3,
            ec=colors[0]
        )
        ax.add_patch(ship_poly)

        x = df[[
            'x [m]', 'u [m/s]',
            'y [m]', 'vm [m/s]',
            'psi [rad]', 'r [rad/s]'
        ]].to_numpy()[step, :]

        rudder1_poly = plt.Polygon(
            rudder_s_coo(x, u, Lpp, B),
            ec=colors[0],
            linewidth=0.3,
            alpha=0.8
        )
        ax.add_patch(rudder1_poly)

        x = df[[
            'x [m]', 'u [m/s]',
            'y [m]', 'vm [m/s]',
            'psi [rad]', 'r [rad/s]'
        ]].to_numpy()[step, :]

        rudder2_poly = plt.Polygon(
            rudder_p_coo(x, u, Lpp, B),
            ec=colors[0],
            linewidth=0.3,
            alpha=0.8
        )
        ax.add_patch(rudder2_poly)

    # trajectory
    ax.plot(
        df['y [m]'], df['x [m]'],
        color=colors[0],
        ls='dashed',
        lw=0.4,
        alpha=0.9
    )


def velo_plot(ax, df, columns, colors, xlabel="$t \ \mathrm{[s]}$", ylabel=None, legend_flag=False):
    # ax setting
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # main plot
    velo = ax.plot(
        df.index,
        df[columns[0]],
        color=colors[0],
        linestyle="solid",
        linewidth=1.0,
    )
    if legend_flag:
        ax.legend()


def pos_plot(ax, df, columns, colors, xlabel="$t \ \mathrm{[s]}$", ylabel=None, legend_flag=False):
    return velo_plot(ax, df, columns, colors, xlabel=xlabel, ylabel=ylabel, legend_flag=legend_flag)


def control_plot(ax, df, columns, colors, labels, xlabel="$t \ \mathrm{[s]}$", ylabel=None, legend_flag=False):
    # ax setting
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # main plot
    # control = ax.plot(
    #     df.index,
    #     df[columns[0]],
    #     color=colors[0],
    #     linestyle="solid",
    #     linewidth=1.0,
    #     label=labels[0]
    # )
    control_r = ax.plot(
        df.index,
        df[columns[0]],
        color=colors[1],
        linestyle="dashed",
        linewidth=1.0,
        label=labels[1]
    )
    #
    if legend_flag:
        ax.legend(bbox_to_anchor=(0.0, 1.05), loc='lower left')


def control_plot_2(ax, df, columns, colors, labels, xlabel="$t \ \mathrm{[s]}$", ylabel=None):
    # ax setting
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # main plot
    ax.plot(
        df.index,
        df[columns[0]],
        color=colors[0],
        linestyle="solid",
        linewidth=1.0,
        label=labels[0]
    )

    

