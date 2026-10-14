"""Plotting helpers for the Arctic training notebooks."""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

def plot_arctic_map(data, title, ax=None, step=4,
                    cmap="RdYlBu_r", vmin=-2, vmax=6,
                    bbox=[-180, 180, 58, 90],
                    cbar_kwargs=None, **plot_kwargs):
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
    cmap : str or matplotlib Colormap, optional
        Colour map used for the field. Default is "viridis".
    vmin, vmax : float, optional
        Limits of the colour scale. If None, xarray picks them from the data.
    cbar_kwargs : dict, optional
        Options for the colour bar (label, shrink, orientation...).
    **plot_kwargs
        Any other option passed to xarray's plot function.

    Returns
    -------
    ax : cartopy GeoAxes
        The map, so that it can be customised further.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": ccrs.NorthPolarStereo()})
    if cbar_kwargs is None:
        cbar_kwargs = {"shrink": 0.7}

    lighter_data = data.isel({dim: slice(None, None, step) for dim in data.dims})
    lighter_data.plot(
        ax=ax,
        transform=ccrs.PlateCarree(),
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        cbar_kwargs=cbar_kwargs,
        **plot_kwargs,
    )

    ax.set_extent(bbox, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor="lightgrey", zorder=0)
    ax.coastlines(linewidth=0.5)
    ax.gridlines(linestyle=":", linewidth=0.5)
    ax.set_title(title)
    return ax

def create_two_arctic_maps():
    """Create a figure with two empty maps centred on the North Pole, side by side.

    Returns
    -------
    ax_left, ax_right : cartopy GeoAxes
        The two maps, to pass to `plot_arctic_map` with `ax=`.
    """
    _, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(14, 6), layout="constrained",
        subplot_kw={"projection": ccrs.NorthPolarStereo()},
    )
    return ax_left, ax_right

def plot_depth_section(
    data,
    latitude,
    title,
    cbar_label,
    ax=None,
    cmap="RdYlBu_r",
    vmin=None,
    vmax=None,
    contour_level=None,
):
    """Plot a vertical section (depth x longitude) of a field at a given latitude.

    Parameters
    ----------
    data : xarray.DataArray
        Field with dimensions depth, latitude and longitude. A time dimension
        is allowed if it holds a single value.
    latitude : float
        Latitude of the section. The nearest grid latitude is used.
    title : str
        Title of the plot.
    cbar_label : str
        Label of the colour bar, e.g. "Sea temperature (°C)".
    ax : matplotlib Axes, optional
        Existing axes to draw on. If None, a new figure is created.
    cmap : str, optional
        Colour map. Default is "RdYlBu_r".
    vmin, vmax : float, optional
        Limits of the colour scale. If None, xarray picks them from the data.
    contour_level : float, optional
        If given, draw a black line where the field equals this value.

    Returns
    -------
    ax : matplotlib Axes
        The plot, so that it can be customised further.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(12, 5))

    section = data.sel(latitude=latitude, method="nearest")
    if "time" in section.dims:
        section = section.squeeze("time")

    section.plot(
        ax=ax, x="longitude", y="depth", yincrease=False,
        cmap=cmap, vmin=vmin, vmax=vmax,
        cbar_kwargs={"label": cbar_label},
    )
    if contour_level is not None:
        section.plot.contour(
            ax=ax, x="longitude", y="depth", yincrease=False,
            levels=[contour_level], colors="black",
        )

    ax.set_title(title)
    plt.show()
    return None