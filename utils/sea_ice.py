"""Helpers for the sea ice reanalysis (ARCTIC_MULTIYEAR_PHY_ICE_002_016) on its original grid."""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

# The original grid of the product is a polar stereographic projection on a sphere,
# described in the product metadata as:
# +proj=stere +lat_0=90 +lat_ts=90 +lon_0=-45 +R=6378273
EARTH_RADIUS_M = 6378273
NEXTSIM_PROJECTION = ccrs.Stereographic(
    central_latitude=90,
    central_longitude=-45,
    true_scale_latitude=90,
    globe=ccrs.Globe(semimajor_axis=EARTH_RADIUS_M, semiminor_axis=EARTH_RADIUS_M, ellipse=None),
)

_UNIT_TO_METRES = {"m": 1.0, "meter": 1.0, "meters": 1.0, "metre": 1.0, "metres": 1.0, "km": 1e3, "100km": 1e5}


def grid_cell_area_km2(dataset):
    """Return the true area of each grid cell, in km².

    On a polar stereographic map, distances are exact at the North Pole and slightly
    stretched further south. A 3 km x 3 km cell of the grid therefore covers a bit
    less than 9 km² on Earth away from the pole. This function corrects for it.

    Parameters
    ----------
    dataset : xarray.Dataset or xarray.DataArray
        Data on the original grid, with coordinates "x" and "y".

    Returns
    -------
    xarray.DataArray
        Area of each cell in km², with dimensions (y, x).
    """
    units = str(dataset["x"].attrs.get("units", "m")).replace(" ", "").lower()
    to_metres = _UNIT_TO_METRES.get(units, 1.0)

    x = dataset["x"] * to_metres
    y = dataset["y"] * to_metres
    spacing = float(abs(x[1] - x[0]))

    distance_to_pole = np.sqrt(x**2 + y**2)
    latitude = np.pi / 2 - 2 * np.arctan(distance_to_pole / (2 * EARTH_RADIUS_M))
    scale_factor = 2 / (1 + np.sin(latitude))

    area = (spacing / scale_factor) ** 2 / 1e6
    area.name = "cell_area"
    area.attrs = {"units": "km2", "long_name": "Area of the grid cell"}
    return area.transpose("y", "x")


def plot_nextsim_map(data, title, ax=None, step=4, **plot_kwargs):
    """Plot a 2D field of the original grid (y x x) on a map of the Arctic.

    Parameters
    ----------
    data : xarray.DataArray
        Field to plot, with dimensions y and x.
    title : str
        Title of the map.
    ax : cartopy GeoAxes, optional
        Existing map, created with projection=NEXTSIM_PROJECTION. If None, a new figure is created.
    step : int, optional
        Keep one grid point out of `step` in each direction, to plot faster.
    **plot_kwargs
        Options passed to xarray's plot function (cmap, vmin, vmax, cbar_kwargs...).
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": NEXTSIM_PROJECTION})

    lighter_data = data.isel(x=slice(None, None, step), y=slice(None, None, step))
    units = str(data["x"].attrs.get("units", "m")).replace(" ", "").lower()
    to_metres = _UNIT_TO_METRES.get(units, 1.0)
    lighter_data = lighter_data.assign_coords(x=lighter_data["x"] * to_metres, y=lighter_data["y"] * to_metres)

    lighter_data.plot(ax=ax, x="x", y="y", transform=NEXTSIM_PROJECTION, **plot_kwargs)
    ax.set_extent([-180, 180, 60, 90], crs=ccrs.PlateCarree())
    ax.coastlines(linewidth=0.5)
    ax.gridlines(linestyle=":", linewidth=0.5)
    ax.set_title(title)
    return ax
