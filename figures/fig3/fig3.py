## Scientific computing stuff
# import sklearn
import numpy as np
import pandas as pd
import geopandas as gpd

from shapely.geometry import Polygon, box, shape

## Plotting stuff
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, ListedColormap, LogNorm
from matplotlib.markers import MarkerStyle
from matplotlib.lines import Line2D
import seaborn as sns
# from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,mark_inset)
# from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib.cm import get_cmap
from matplotlib import animation, rc

import alphashape

from PIL import Image

name = "tab10"
cmap = get_cmap(name)
colors = [c for i,c in enumerate(cmap.colors) if i!=7]

propro = pd.read_csv("propro.csv")
osm_df = gpd.read_file("osm_df.geojson")
hk_gadm = gpd.read_file("../fig2/hk_gadm.geojson")
hk_gadm = hk_gadm.to_crs("epsg:4326")
osm_df = osm_df.to_crs("epsg:4326")

fig, ax = plt.subplots(figsize=(24,24))
hk_gadm.plot(edgecolor="#AAAAAA", color="#FFFFFF", ax=ax)
fig.set_facecolor('#AAAAAA')
scats = []
texts = []
plt.xticks([])
plt.yticks([])
ax.axis("off")
plt.ylim([22.275,22.35])
plt.xlim([114.1,114.25])

osm_df.plot(color="#DDDDDD", edgecolor="#AAAAAA", ax=ax)

for ii,cl in enumerate(propro.cl.unique()):
    cl_sub = propro.loc[propro.cl == cl]
    if len(cl_sub.cl) > 1:
        points_2d = np.array(list(zip(cl_sub.lng, cl_sub.lat)))
        alpha_shape = alphashape.alphashape(points_2d, 20.0)
        try:
            alpha_shape = np.array(alpha_shape.exterior.coords.xy)
            
            polygon_geom = Polygon(zip(alpha_shape[0], alpha_shape[1])).buffer(0.002)
            polygon = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon_geom]) 
            
            polygon.plot(ax=ax, color=colors[ii%len(colors)], alpha=0.5, edgecolor="black", linewidth=1)
            ax.scatter(cl_sub.lng.tolist(), cl_sub.lat.tolist(), 
                       color=colors[ii%len(colors)], marker="o", s=200,
                       edgecolors="black", linewidth=2)
        except Exception as e:
            print(e)
    else:
        ax.scatter(cl_sub.lng.tolist(), cl_sub.lat.tolist(), 
                       color=colors[ii%len(colors)], marker="o", s=200,
                       edgecolors="black", linewidth=2)


legend_elements = [Line2D([0], [0], marker='o', color='w', linewidth=0, label='Protest report',
                          markerfacecolor='w', markeredgecolor="black", markersize=20),]

ax.legend(handles=legend_elements, loc='center left',prop={'size': 25})
plt.savefig("fig3_large.jpg",bbox_inches='tight',pad_inches=0,dpi=300)

base_width = 300 * 6.5
img = Image.open('fig3_large.jpg')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((round(base_width), round(hsize)), resample=Image.LANCZOS)
img.save('fig3.jpg')