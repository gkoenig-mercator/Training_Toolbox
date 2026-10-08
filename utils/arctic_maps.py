"""Plotting helpers for the Arctic training notebooks."""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


def plot_arctic_map(data, title, ax=None, step=4, **plot_kwargs):
    """Plot a 2D field (latitude x longitude) on a map centred on the North Pole.

    Parameters
    ----------
    data : xarray.DataArray
        Field to plot, with two dimensions (latitude and longitude).
    title : str
        Title of the map.
    ax : cartopy GeoAxes, optional
        Existing map to draw on. If None, a new figure is created.
    step : int, optional
        Keep one grid point out of `step` in each direction, to plot faster.
        Use step=1 to plot every grid point.
    **plot_kwargs
        Options passed to xarray's plot function (cmap, vmin, vmax, cbar_kwargs...).

    Returns
    -------
    ax : cartopy GeoAxes
        The map, so that it can be customised further.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": ccrs.NorthPolarStereo()})

    lighter_data = data.isel({dim: slice(None, None, step) for dim in data.dims})
    lighter_data.plot(ax=ax, transform=ccrs.PlateCarree(), **plot_kwargs)

    ax.set_extent([-180, 180, 58, 90], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor="lightgrey", zorder=0)
    ax.coastlines(linewidth=0.5)
    ax.gridlines(linestyle=":", linewidth=0.5)
    ax.set_title(title)
    return ax
