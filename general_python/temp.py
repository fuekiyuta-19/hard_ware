import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import matplotlib.ticker as ptick

from subroutine import font_set, plottool, ship_shape
font_set.fig_eekanji()

t = [0, 1, 1, 4, 4, 10]
v = [0, 0, 0.01, 0.01, 0.03, 0.03]
t_lab = [0, 1, 4]
y_tick = [0, 0.01, 0.02, 0.03]

fig = pyplot.figure(figsize = (15.2, 9.6), dpi = 100, linewidth = 0, edgecolor = 'w')
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylabel("$v_{0}~ [\mathrm{m/s}]$", fontsize = 38)
ax1.step(t, v, color = 'blue', label = "Reference speed")
ax1.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))   # こっちを先に書くこと。
ax1.ticklabel_format(style="sci", axis="y", scilimits=(3,-3))   # 10^3単位の指数で表示する。
ax1.set_xlim(0, 6)
ax1.set_yticks(y_tick)
ax1.set_yticklabels(y_tick, fontsize = 28)
ax1.axes.xaxis.set_visible(False)
ax1.grid()
ax1.legend(loc ='upper left', fontsize = 40)
plt.savefig("general_python/datalist/test/" + "ref_speed" + '.png')