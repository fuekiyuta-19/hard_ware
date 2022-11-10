from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from subroutine import font_set

font_set.fig_eekanji()

delta_port = np.array([-80, -80, -80, -75, -75, -75, -70, -70, -70])
delta_ster = np.array([70, 75, 80, 70, 75, 80, 70, 75, 80])
X          = np.array([0.0735, -0.0620, -0.2061, 0.1298, -0.0063, -0.1089, 0.3724, 0.1380, 0.0030])
Y          = np.array([-0.04, -0.0482, 0.0507, 0.0544, 0.0655, 0.1816, 0.1152, 0.1552, 0.2678])

plot_port = [delta_port[2], delta_port[8], delta_port[6], delta_port[0], delta_port[2]]
plot_ster = [delta_ster[2], delta_ster[8], delta_ster[6], delta_ster[0], delta_ster[2]]
plot_X    = [X[2], X[8], X[6], X[0], X[2]]
plot_Y    = [Y[2], Y[8], Y[6], Y[0], Y[2]]

fig1 = plt.figure(figsize = (9, 8))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.set_ylabel("$\delta_{\mathrm{p}}$ [deg]", size = 25, color = "black", labelpad = 15)
ax1.set_xlabel("$\delta_{\mathrm{s}}$ [deg]", size = 25, color = "black", labelpad = 15)
ax1.set_zlabel("$X_{\mathrm{CT}} $[N]", size = 25, color = "black", labelpad= 15)
plt.setp(ax1.get_xticklabels(), fontsize=15)
plt.setp(ax1.get_yticklabels(), fontsize=15)
plt.setp(ax1.get_zticklabels(), fontsize=15)
ax1.scatter(delta_ster, delta_port, X, label = "CFD")
ax1.plot(plot_ster, plot_port, plot_X, "-", color="#00aa00", ms=4, mew=0.5)
ax1.legend(fontsize = 25)
plt.tight_layout()
plt.savefig("general_python/datalist/3dfig/3dfig_x.png")

fig2 = plt.figure(figsize = (9, 8))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_xlabel("$\delta_{\mathrm{p}}$ [deg]", size = 25, color = "black", labelpad = 15)
ax2.set_ylabel("$\delta_{\mathrm{s}}$ [deg]", size = 25, color = "black", labelpad = 15)
ax2.set_zlabel("$Y_{\mathrm{CT}}$[N]", size = 25, color = "black", labelpad = 15)
plt.setp(ax2.get_xticklabels(), fontsize=15)
plt.setp(ax2.get_yticklabels(), fontsize=15)
plt.setp(ax2.get_zticklabels(), fontsize=15)
ax2.scatter(delta_port, delta_ster, Y, label = "CFD")
ax2.plot(plot_port, plot_ster, plot_Y, "-", color="#00aa00", ms=4, mew=0.5)
ax2.legend(fontsize = 25)
plt.tight_layout()
plt.savefig("general_python/datalist/3dfig/3dfig_y.png")

print("Task Finish")