import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# Try to use Chinese-capable font
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Data from user
data = np.array([
    [0.1675,    0.091528,  0.025556,  -0.023333,  -0.014028,  0.022778,   0.090833,   0.183889,   0.356111,   0.518472],
    [0.168194,  0.110833,  0.054861,  -0.006111,   0.0,        0.072222,   0.104722,   0.191944,   0.32125,    0.467917],
    [0.178611,  0.082361,  0.020972,   0.000694,   0.016806,   0.070417,   0.110139,   0.201528,   0.346528,   0.440417],
    [0.189444,  0.065,     0.017361,  -0.007083,  -0.004861,  0.066667,   0.130417,   0.189583,   0.314306,   0.482778],
    [0.152083,  0.040972,  0.030694,  -0.003889,  0.013194,   0.036667,   0.109306,   0.204028,   0.311111,   0.455139],
    [0.11875,   0.011111, -0.017083,  -0.031389,  -0.010278,  0.030417,   0.089861,   0.192778,   0.306528,   0.457222],
    [0.074722, -0.04125,  -0.079861,  -0.079306,  -0.078889,  -0.016111,  0.056528,   0.156389,   0.298056,   0.44],
    [0.026806, -0.095417, -0.123194,  -0.159722,  -0.139306,  -0.094167,  -0.023194,  0.111389,   0.222917,   0.390417],
    [-0.044861,-0.140833, -0.216944,  -0.248889,  -0.250139,  -0.155556,  -0.110278,  0.000556,   0.166806,   0.323194],
    [-0.112083,-0.232778, -0.311944,  -0.332778,  -0.312361,  -0.264167,  -0.187222,  -0.073472,  0.080833,   0.268472],
])

row_labels = ['Y=349.92', 'Y=311.04', 'Y=272.16', 'Y=233.28', 'Y=194.40',
              'Y=155.52', 'Y=116.64', 'Y=77.76', 'Y=38.88', 'Y=0.00']
col_labels = ['X=0.00', 'X=35.55', 'X=71.10', 'X=106.65', 'X=142.20',
              'X=177.75', 'X=213.30', 'X=248.85', 'X=284.40', 'X=319.95']

fig, ax = plt.subplots(figsize=(12.5, 6))

# Custom colormap: cyan -> green -> yellow -> orange -> red (like reference)
colors_list = [
    '#00CFFF', '#00E5FF', '#4DEEEA',
    '#7FFF00', '#ADFF2F', '#FFFF00',
    '#FFD700', '#FFA500', '#FF8C00',
    '#FF4500', '#FF0000', '#CC0000'
]
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors_list)

im = ax.imshow(data, cmap=cmap, vmin=-0.35, vmax=0.55, aspect='auto')

# Set ticks
ax.set_xticks(np.arange(len(col_labels)))
ax.set_yticks(np.arange(len(row_labels)))
ax.set_xticklabels(col_labels, fontsize=10)
ax.set_yticklabels(row_labels, fontsize=10)

# X labels on top
ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False,
               length=0)  # remove tick marks

# Add grid lines between cells
ax.set_xticks(np.arange(-.5, len(col_labels), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(row_labels), 1), minor=True)
ax.grid(which="minor", color="white", linestyle='-', linewidth=1.5)

# Border styling
for spine in ['left', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['top', 'bottom']:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_linewidth(2)

# Text annotations with dynamic color for readability
for i in range(len(row_labels)):
    for j in range(len(col_labels)):
        val = data[i, j]
        # Use white text for extreme values, black for moderate values
        if val < -0.22 or val > 0.42:
            tc = 'white'
        else:
            tc = 'black'
        ax.text(j, i, f'{val:.6f}', ha='center', va='center', color=tc,
                fontsize=10, fontfamily='monospace', fontweight='bold')

# "行\列" header in the top-left corner (like reference image)
ax.text(-0.65, -0.5, r'行\列', ha='center', va='center',
        fontsize=13, fontweight='bold')

fig.tight_layout()

output_path = 'c:/Users/HP/CodeBuddy/20260630095547/probe_matrix.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.15)
print(f'Saved to {output_path}')
