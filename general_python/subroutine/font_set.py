import matplotlib.pyplot as plt

def fig_eekanji():
    plt.rcParams["font.family"]  = "serif"       # 使用するフォント
    plt.rcParams["font.serif"]   = "Times New Roman"
    plt.rcParams["font.size"]    = 12             # 基本となるフォントの大きさ
    plt.rcParams["mathtext.cal"] = "serif"      # TeX表記に関するフォント設定
    plt.rcParams["mathtext.rm"]  = "serif"       # TeX表記に関するフォント設定
    plt.rcParams["mathtext.it"]  = "serif:italic"# TeX表記に関するフォント設定
    plt.rcParams["mathtext.bf"]  = "serif:bold"  # TeX表記に関するフォント設定
    plt.rcParams["mathtext.fontset"] = "cm"     # TeX表記に関するフォント設定
    # figure grid
    plt.rcParams["axes.grid"]      = True            # Whether to show the grid
    plt.rcParams["grid.color"]     = "darkgray"        # Grid color
    plt.rcParams["grid.linewidth"] = 0.05       # Grid width
    # fig Tick and scale
    # Scale line orientation, inner "in" or outer "out" or both "inout"
    plt.rcParams["xtick.direction"] = "in"
    # Scale line orientation, inner "in" or outer "out" or both "inout"
    plt.rcParams["ytick.direction"] = "in"
    # Whether to draw a scale line at the top
    plt.rcParams["xtick.top"] = True
    # Whether to draw a scale line at the bottom
    plt.rcParams["xtick.bottom"] = True
    # Whether to draw a scale line at the left
    plt.rcParams["ytick.left"] = True
    # Whether to draw a scale line at the right
    plt.rcParams["ytick.right"] = True
    # whether to draw x-axis minor tick marks
    plt.rcParams["xtick.minor.visible"] = True
    # whether to draw y-axis minor tick marks
    plt.rcParams["ytick.minor.visible"] = True
    # legend setting
    plt.rcParams["legend.frameon"]  = True
    plt.rcParams["legend.fancybox"] = False
    # Line thickness around the graph
    plt.rcParams["axes.linewidth"]  = 0.5
    plt.rcParams["lines.linewidth"] = 0.5
    # set color map
#     plt.rcParams['axes.prop_cycle']  = cycler(color=[‘#03AF7A’, ‘#005AFF’, ‘#4DC4FF’, ‘#FF8082’,‘#F6AA00’,
#                                                 ‘#990099’,‘#804000’,‘#FF4B00’,‘#FFF100’])