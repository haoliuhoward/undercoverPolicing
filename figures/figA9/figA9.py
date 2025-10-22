import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
from shapely.geometry import Polygon, box, shape
from math import cos
from PIL import Image

def make_box(lat, lon, km=1):
    lat_delta = (360/40075)*km/2
    lon_delta = (360 / (cos(lat) * 40075))*km/2
    pgon = Polygon(zip([lon-lon_delta, lon-lon_delta, lon+lon_delta, lon+lon_delta],
                       [lat-lat_delta, lat+lat_delta, lat+lat_delta, lat-lat_delta]))
    return pgon

kowloon = make_box(22.330539918627873, 114.16136399637702, km=2)
crs = {'init': 'epsg:4326'}
kowloon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[kowloon])

mountains = make_box(22.374607253576954, 114.05248509432099, km=2)
crs = {'init': 'epsg:4326'}
mountains = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[mountains])

parkcentral = make_box(22.3117404172, 114.25900641999606, km=2)
crs = {'init': 'epsg:4326'}
parkcentral = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[parkcentral])

hk_dcca = gpd.read_file("hk_dcca.geojson")
hk_gadm = gpd.read_file("../fig2/hk_gadm.geojson")

hk_dcca = hk_dcca.to_crs("epsg:4326")
hk_gadm = hk_gadm.to_crs("epsg:4326")

fig = plt.figure(figsize=(20,20))

gs0 = fig.add_gridspec(2,2)

ax1 = fig.add_subplot(gs0[0])
ax2 = fig.add_subplot(gs0[1])
ax3 = fig.add_subplot(gs0[2])
ax4 = fig.add_subplot(gs0[3])

out = gpd.clip(hk_dcca, hk_gadm)
out = out.to_crs(epsg=4326)
out.boundary.plot(figsize=(8,8), linewidth=1, edgecolor="#666666", ax=ax1, zorder=1)

mountains.plot(ax=ax1, facecolor="#FF000033", edgecolor="red", linewidth=4, zorder=2)
kowloon.plot(ax=ax1, facecolor="#0000FF33", edgecolor="blue", linewidth=4, zorder=2)
parkcentral.plot(ax=ax1, facecolor="#00FF0033", edgecolor="green", linewidth=4, zorder=2)

clipit1 = gpd.clip(out, mountains)
clipit1 = clipit1.to_crs(epsg="3857")

clipit2 = gpd.clip(out, kowloon)
clipit2 = clipit2.to_crs(epsg="3857")

clipit3 = gpd.clip(out, parkcentral)
clipit3 = clipit3.to_crs(epsg="3857")

clipit1.boundary.plot(ax=ax2, edgecolor=None, alpha=0, figsize=(8,8), zorder=1)
ctx.add_basemap(ax=ax2, url=ctx.providers.OpenStreetMap.HOT)
clipit1.plot(ax=ax2, facecolor="none", edgecolor="black", linewidth=4, alpha=1)

clipit2.boundary.plot(ax=ax3, edgecolor=None, alpha=0, figsize=(8,8), zorder=1)
ctx.add_basemap(ax=ax3, url=ctx.providers.OpenStreetMap.HOT)
clipit2.plot(ax=ax3, facecolor="none", edgecolor="black", linewidth=4, alpha=1)

clipit3.boundary.plot(ax=ax4, edgecolor=None, alpha=0, figsize=(8,8), zorder=1)
ctx.add_basemap(ax=ax4, url=ctx.providers.OpenStreetMap.HOT)
clipit3.plot(ax=ax4, facecolor="none", edgecolor="black", linewidth=4, alpha=1)

ax1.axis("off")
ax2.axis("off")
ax3.axis("off")
ax4.axis("off")

plt.show()

plt.savefig("figA9_large.jpg",transparent=True,bbox_inches="tight",dpi=300)

base_width = 300 * 6.5
img = Image.open('figA9_large.jpg')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((round(base_width), round(hsize)), resample=Image.LANCZOS)
img.save('figA9.jpg')