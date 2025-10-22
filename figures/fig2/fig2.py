import geopandas as gpd

import numpy as np

import contextily as ctx

## Plotting stuff
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, ListedColormap, LogNorm
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

import seaborn as sns

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, InsetPosition, mark_inset
from mpl_toolkits.axes_grid1 import make_axes_locatable

from PIL import Image

# Choose colormap
cmap = pl.cm.plasma_r
# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))
# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)
my_cmap[:,-1] = 1
my_cmap[0,-1] = 0
my_cmap = my_cmap[range(0,round(0.75*my_cmap.shape[0])),:]
# Create new colormap
my_cmap = ListedColormap(my_cmap)

## Load data
hkp_seige = gpd.read_file("hkp_seige.geojson")
hk_gadm = gpd.read_file("hk_gadm.geojson")
grid = gpd.read_file("grid.geojson")
hk_hwy = gpd.read_file("hk_hwy.geojson")
hwy_hkp = gpd.read_file("hwy_hkp.geojson")

## Make sure data are projected properly
grid = grid.to_crs(epsg=3857)
hk_hwy = hk_hwy.to_crs(epsg=3857)
hk_gadm = hk_gadm.to_crs(epsg=3857)
hwy_hkp = hwy_hkp.to_crs(epsg=3857)

ax = grid.plot(column="col", cmap=my_cmap, edgecolor=None, linewidth=0, figsize=(20,20), zorder=1)
hk_gadm.plot(ax=ax, color="none", edgecolor="black", linewidth=1, zorder=3)
hk_hwy.plot(ax=ax, edgecolor="black", alpha=1, zorder=2, linewidth=0.5)
ctx.add_basemap(ax=ax, url=ctx.providers.CartoDB.PositronNoLabels)

plt.axis("off")

sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=LogNorm(vmin=1.0, vmax=np.power(10,grid["col"].max())+1))
sm._A = []
divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="2.5%", pad=0.05)
cbar = plt.colorbar(sm, cax=cax, orientation="horizontal")
cbar.ax.tick_params(labelsize=24) 

###############
## INSET
###############
# Create a set of inset Axes: these should fill the bounding box allocated to them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax, [0.45,0.45,0.72,0.57])
ax2.set_axes_locator(ip)

hwy_hkp.plot(ax=ax2, edgecolor=None, alpha=0.0, figsize=(20,20))
ctx.add_basemap(ax=ax2, source=ctx.providers.CartoDB.PositronNoLabels)#OpenMapSurfer.Roads)
hkp_seige.plot(ax=ax2, color="#DE5849", edgecolors="#240047", alpha=0.75, markersize=42)
ax2.get_xaxis().set_ticks([])
ax2.get_yaxis().set_ticks([])
ax2.spines['bottom'].set_color('black')
ax2.spines['top'].set_color('black')
ax2.spines['right'].set_color('black')
ax2.spines['left'].set_color('black')
ax2.spines['bottom'].set_linewidth(2)
ax2.spines['top'].set_linewidth(2)
ax2.spines['right'].set_linewidth(2)
ax2.spines['left'].set_linewidth(2)

# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax, ax2, loc1=2, loc2=4, fc="#FFFFFF99", ec='black', linewidth=2, zorder=5)

plt.savefig("fig2_large.jpg",transparent=True,bbox_inches="tight",dpi=300)

base_width = 300 * 6.5
img = Image.open('fig2_large.jpg')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((round(base_width), round(hsize)), resample=Image.LANCZOS)
img.save('fig2.jpg')