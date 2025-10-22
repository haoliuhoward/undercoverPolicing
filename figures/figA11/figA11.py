import geopandas as gpd
import matplotlib.pyplot as plt

grid = gpd.read_file("grid.geojson")

fig, ax = plt.subplots(dpi=300, figsize=(6.5,6.5))

grid.plot(ax=ax,color="white",linewidth=1,edgecolor="black")
ax.set_axis_off();

plt.savefig("figA11.jpg", bbox_inches="tight")