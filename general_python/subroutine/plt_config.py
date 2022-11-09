
import matplotlib.pyplot as plt

def set_rcParams():
    plt.rcParams["font.family"] = "serif"       # Font
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams["font.size"] = 10              # Basic size of font
    plt.rcParams["mathtext.cal"] = "serif"      # Font for TeX
    plt.rcParams["mathtext.rm"] = "serif"       # Font for TeX
    plt.rcParams["mathtext.it"] = "serif:italic"  # Font for TeX
    plt.rcParams["mathtext.bf"] = "serif:bold"  # Font for TeX
    plt.rcParams["mathtext.fontset"] = "cm"     # Font for TeX
    
    plt.rcParams['mathtext.fontset'] = "stix"
    
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams["xtick.major.size"] = 2.0
    plt.rcParams["ytick.major.size"] = 2.0
    plt.rcParams["xtick.major.width"] = 0.5
    plt.rcParams["ytick.major.width"] = 0.5
    plt.rcParams["xtick.minor.size"] = 0.6
    plt.rcParams["ytick.minor.size"] = 0.6
    plt.rcParams["xtick.minor.width"] = 0.3
    plt.rcParams["ytick.minor.width"] = 0.3
    plt.rcParams['xtick.direction'] = "in"        
    plt.rcParams['ytick.direction'] = "in"             
    
    plt.rcParams["axes.grid"] = True
    plt.rcParams["axes.labelsize"] = 20
    plt.rcParams["axes.linewidth"] = 0.5
    
    plt.rcParams["grid.color"] = "gray"
    plt.rcParams["grid.linewidth"] = 0.050
    
    plt.rcParams["legend.facecolor"] = "white"
    plt.rcParams['legend.edgecolor'] = "black"
    plt.rcParams["legend.fancybox"] = True
    plt.rcParams["legend.framealpha"] = 0.70

    plt.rcParams["figure.subplot.wspace"] = 0.60
    plt.rcParams["figure.subplot.hspace"] = 0.30

    plt.rcParams['lines.linewidth'] = 0.80

