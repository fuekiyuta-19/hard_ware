
import os
import sys
sys.path.append(os.getcwd())

from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from subroutine.ship_shape import ship_coo, rudder_s_coo, rudder_p_coo
from subroutine.font import font_setting
font_setting()

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

class SetFigure:
    def __init__(self, fig_size, dpi, colors):
        self.fig_size = fig_size
        self.fig      = plt.figure(figsize=self.fig_size)
        self.dpi      = dpi
        self.colors   = colors
        self.axs      = [None]*11
        self.make_axes()

    def make_axes(self):
        gs_master = GridSpec(nrows=4, ncols=4, height_ratios=[1, 1, 1, 1])

        gs_1    = GridSpecFromSubplotSpec(
            nrows=3, ncols=2, subplot_spec=gs_master[0:3, 0:2]
        )
        gs_234  = GridSpecFromSubplotSpec(
            nrows=3, ncols=1, subplot_spec=gs_master[0:3, 2]
        )
        gs_567  = GridSpecFromSubplotSpec(
            nrows=3, ncols=1, subplot_spec=gs_master[0:3, 3]
        )
        gs_8901 = GridSpecFromSubplotSpec(
            nrows=1, ncols=4, subplot_spec=gs_master[3, :]
        )

        self.axs[0] = self.fig.add_subplot(gs_1[:,:])
        self.axs[1] = self.fig.add_subplot(gs_234[0,:])
        self.axs[2] = self.fig.add_subplot(gs_234[1,:])
        self.axs[3] = self.fig.add_subplot(gs_234[2,:])
        self.axs[4] = self.fig.add_subplot(gs_567[0,:])
        self.axs[5] = self.fig.add_subplot(gs_567[1,:])
        self.axs[6] = self.fig.add_subplot(gs_567[2,:])
        self.axs[7] = self.fig.add_subplot(gs_8901[:,0])
        self.axs[8] = self.fig.add_subplot(gs_8901[:,1])
        self.axs[9] = self.fig.add_subplot(gs_8901[:,2])
        self.axs[10] = self.fig.add_subplot(gs_8901[:,3])



class SetData:
    def __init__(self, csv_pathes, obs_df, Lpp):
        dfs = []
        dfs_len = []
        for csv in csv_pathes:
            df = self.convert(csv, Lpp)
            dfs.append(df)
            dfs_len.append(len(df))

        self.dfs = dfs
        self.frames = max(dfs_len)
        # self.frames = 20
        self.obs_df = pd.read_csv(obs_df) / Lpp
        
    def convert(self, csv, Lpp):
        df = pd.read_csv(csv)
        df.iloc[:,1] = df.iloc[:, 1] / Lpp       # m -> Lpp
        df.iloc[:,2] = df.iloc[:, 2] * 0.5144    # kts -> m/s
        df.iloc[:,3] = df.iloc[:, 3] / Lpp       # m -> Lpp
        df.iloc[:,4] = df.iloc[:, 4] * 0.5144    # kts -> m/s
        df.iloc[:,5] = np.rad2deg(df.iloc[:,5])  # rad -> deg.
        df.iloc[:,6] = np.rad2deg(df.iloc[:,6])  # rad -> deg.
        df.iloc[:,7] = np.rad2deg(df.iloc[:,7])  # rad -> deg.
        df.iloc[:,8] = np.rad2deg(df.iloc[:,8])  # rad -> deg.
        return df
        


class SetAnime:
    def __init__(self, dpi,interval, output_dir, output_name):
        self.dpi         = dpi
        self.output_dir  = output_dir
        self.output_name = output_name
        self.interval    = interval


class MakeAnime:
    def __init__(self, setfig, setdata, setanime):
        self.setfig   = setfig
        self.setdata  = setdata
        self.setanime = setanime

    def draw(self):
        anime = animation.FuncAnimation(
            fig      = self.setfig.fig,
            func     = self.update,
            interval = self.setanime.interval,
            frames   = tqdm(range(self.setdata.frames))
        )
        anime.save(
            f'{self.setanime.output_dir}{self.setanime.output_name}.mp4',
            writer='ffmpeg',
            dpi = self.setanime.dpi
        )

        print('~~~~~~~~~~~~~~~~')
        print('Animation Saved.')
        print('~~~~~~~~~~~~~~~~')

    def update(self, frame):
        for ax in self.setfig.axs:
            ax.cla()
        
        for i in range(len(self.setdata.dfs)):
            self.plot(frame, self.setfig.colors, i)
        
        self.setfig.fig.tight_layout()

    def plot(self, frame, colors, i):
        # traj
        traj_plot(
            ax      = self.setfig.axs[0],
            Lpp     = 150.0, 
            B       = 24.3,
            colors  = colors,
            setdata = self.setdata,
            frame   = frame,
            i       = i
        )

        # x, y, psi
        item_plot(
            ax       = self.setfig.axs[1],
            setdata  = self.setdata,
            item_num = 1,
            ylabel   = '$x/L_{\mathrm{pp}}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[2],
            setdata  = self.setdata,
            item_num = 3,
            ylabel   = '$y/L_{\mathrm{pp}}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[3],
            setdata  = self.setdata,
            item_num = 5,
            ylabel   = '$\psi~\mathrm{[deg.]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        # u, vm, r
        item_plot(
            ax       = self.setfig.axs[4],
            setdata  = self.setdata,
            item_num = 2,
            ylabel   = '$u~\mathrm{[m/s]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[5],
            setdata  = self.setdata,
            item_num = 4,
            ylabel   = '$v_{\mathrm{m}}~\mathrm{[m/s]}$',
            colors   = colors,
            frame    = frame,
            i        = i 
        )

        item_plot(
            ax       = self.setfig.axs[6],
            setdata  = self.setdata,
            item_num = 6,
            ylabel   = '$r~\mathrm{[deg./s]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )
        
        # delp, dels, np, iBT
        item_plot(
            ax       = self.setfig.axs[7],
            setdata  = self.setdata,
            item_num = 7,
            ylabel   = '$\delta_{\mathrm{s}}~\mathrm{[deg.]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[8],
            setdata  = self.setdata,
            item_num = 8,
            ylabel   = '$\delta_{\mathrm{p}}~\mathrm{[deg.]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[9],
            setdata  = self.setdata,
            item_num = 9,
            ylabel   = '$n_{\mathrm{p}}~\mathrm{[rps]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )

        item_plot(
            ax       = self.setfig.axs[10],
            setdata  = self.setdata,
            item_num = 10,
            ylabel   = '$i_{\mathrm{BT}}~\mathrm{[mA]}$',
            colors   = colors,
            frame    = frame,
            i        = i
        )




def traj_plot(ax, Lpp, B, colors, setdata, frame, i):
    xlabel = '$y/L_{\mathrm{pp}}$'
    ylabel = '$x/L_{\mathrm{pp}}$'
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_aspect('equal')

    x_min = min(setdata.dfs[i].iloc[:,3]) - 1.0
    x_max = max(setdata.dfs[i].iloc[:,3]) + 1.0
    y_min = min(setdata.dfs[i].iloc[:,1]) - 1.0
    y_max = max(setdata.dfs[i].iloc[:,1]) + 1.0
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # obstacle
    obs_df = setdata.obs_df
    if obs_df.isnull().values.sum() >= 1:
        berth_num_list = list(obs_df[obs_df["X"].isnull()].index.values)
        berth_num_list.append(len(obs_df))

        for k in range(len(berth_num_list)-1):
            berth_df_1 = obs_df[berth_num_list[k]+1 : berth_num_list[k+1]-1]
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
        berth_array = obs_df.values
        pos = []
        for k in range(len(berth_array)-1):
            pos.append(berth_array[k, [0,1]])
        berth_poly = plt.Polygon(
            pos,
            fill=True,
            alpha=1.0,
            linewidth=0.3,
            fc="#C8CCDE",
            ec="#0A0F60"
        )
        berth = ax.add_patch(berth_poly)
    
    # ship
    x = setdata.dfs[i].iloc[:,1:7].to_numpy()[frame]
    u = setdata.dfs[i].iloc[:,7:11].to_numpy()[frame]

    ship_poly = plt.Polygon(
        ship_coo(x, Lpp, B)[:, [1,0]],
        fill = False,
        alpha=0.8,
        linewidth=0.3,
        color=colors[i],
        zorder=100
    )
    ax.add_patch(ship_poly)
    

    # traj
    ax.plot(
        setdata.dfs[i].iloc[:,3], setdata.dfs[i].iloc[:,1],
        ls = 'dashed',
        lw = 0.5,
        color=colors[i]
    )


def item_plot(ax, setdata, item_num, ylabel, colors, frame, i):
    ax.set_xlabel('$t~\mathrm{[s]}$')
    ax.set_ylabel(ylabel)
    
    ax.plot(
        setdata.dfs[i].index, setdata.dfs[i].iloc[:, item_num],
        color=colors[i],
        linestyle="solid",
        linewidth=1.0
    )

    ax.axvline(
        x=setdata.dfs[i].index[frame],
        lw=0.3,
        c='k'
    )
    ax.plot(
        setdata.dfs[i].index[frame], setdata.dfs[i].iloc[frame, item_num],
        lw=0.9,
        c=colors[i],
        marker='o',
        zorder=100
    )



class Colors:
    red     = [255 / 330, 75 / 330, 0.0]
    yellow  = [255 / 496, 241 / 496, 0.0]
    green   = [3 / 300, 175 / 300, 122 / 300]
    blue    = [0 / 345, 90 / 345, 255 / 345]
    skyblue = [77 / 528, 196 / 528, 255 / 528]
    shiplightgray = [ 0, 0, 0 ]
    shipgray      = [ 76 / 255, 76 / 255, 76 / 255, ]
    zenithblue    = [ 68 / 255, 150 / 255, 211 / 255 ]



# !!! exe !!! #
if __name__ == 'main':
    setfig = SetFigure(
        fig_size = (1.6*10, 1.0*10),
        dpi     = 350,
        colors  = [Colors.red, Colors.green]
    )

    setdata = SetData(
        csv_pathes = [
            filepath + datanema1[0] + ".csv",
            filepath + datanema2[0] + ".csv"
        ],
        obs_df     = 'general_python/datalist/input_CSV_VR',
        Lpp        = 150
    )

    setanime = SetAnime(
        dpi         = 350,
        interval    = 50, 
        output_dir  = outputpath, 
        output_name = 'test',
    )

    # assemble
    anim = MakeAnime(
        setfig, setdata, setanime
    )
    anim.draw()