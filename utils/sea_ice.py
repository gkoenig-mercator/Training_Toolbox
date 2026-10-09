"""Helpers for the satellite sea ice concentration record (SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009)."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

EARTH_RADIUS_KM = 6371.0


def select_day_each_year(data, month, day):
    """Keep one day per year: the available day closest to the given day of the given month.

    The first years of the record only have data every other day, so the exact
    day is not always available. Nothing is downloaded: the selection is only prepared.
    """
    times = pd.DatetimeIndex(data["time"].values)
    positions = []
    for year in sorted(set(times.year)):
        in_month = np.flatnonzero((times.year == year) & (times.month == month))
        if len(in_month) > 0:
            positions.append(in_month[np.abs(times[in_month].day - day).argmin()])

    # Each day is selected separately, as a slice of one day, and the days are then put
    # together. Selecting all the days at once with a list makes dask read whole blocks
    # of many days around each selected day, which is much slower.
    one_day_slices = [data.isel(time=slice(position, position + 1)) for position in positions]
    return xr.concat(one_day_slices, dim="time")


def _grid_cell_area_km2(concentration):
    """Area of each grid cell, in km²: regular latitude/longitude grid, or equal-area x/y grid."""
    for lat_name, lon_name in [("latitude", "longitude"), ("lat", "lon")]:
        if lat_name in concentration.dims:
            latitude = concentration[lat_name]
            dlat = np.radians(float(abs(latitude[1] - latitude[0])))
            dlon = np.radians(float(abs(concentration[lon_name][1] - concentration[lon_name][0])))
            area = EARTH_RADIUS_KM**2 * dlat * dlon * np.cos(np.radians(latitude))
            return area, [lat_name, lon_name]

    # Equal-area grid (x/y in metres): all the cells have the same area
    dx = float(abs(concentration["x"][1] - concentration["x"][0]))
    dy = float(abs(concentration["y"][1] - concentration["y"][0]))
    return dx * dy / 1e6, ["y", "x"]


def compute_sea_ice_extent(concentration, threshold=15):
    """Compute the sea ice extent for each date, in million km².

    The extent is the total area of the grid cells where the sea ice concentration
    is at least `threshold` percent (15% by default, the usual definition).
    This is the step where the data are actually transferred.
    """
    units = str(concentration.attrs.get("units", "%")).strip().lower()
    threshold_in_data_units = threshold if units in ("%", "percent") else threshold / 100

    cell_area, horizontal_dims = _grid_cell_area_km2(concentration)
    extent = (cell_area * (concentration >= threshold_in_data_units)).sum(dim=horizontal_dims) / 1e6
    extent = extent.compute()

    extent.name = "sea_ice_extent"
    extent.attrs = {
        "units": "million km2",
        "long_name": f"Sea ice extent (concentration of at least {threshold}%)",
    }
    return extent


def plot_extent_trend(extent, label):
    """Plot a sea ice extent time series and its linear trend, and print the trend.

    Call it several times before plt.show() to draw several series on the same figure.
    """
    years = extent["time"].dt.year.values
    slope, intercept = np.polyfit(years, extent.values, 1)
    trend_per_decade = 10 * slope
    mean_extent = float(extent.mean())

    plt.gcf().set_size_inches(12, 5)
    (line,) = plt.plot(years, extent.values, marker="o", label=label)
    plt.plot(years, slope * years + intercept, "--", color=line.get_color(),
             label=f"{label} trend: {trend_per_decade:+.2f} million km² per decade")
    plt.xlabel("Year")
    plt.ylabel("Sea ice extent (million km²)")
    plt.title("Arctic sea ice extent")
    plt.legend()

    print(f"{label}: mean extent {mean_extent:.2f} million km², "
          f"trend {trend_per_decade:+.2f} million km² per decade "
          f"({100 * trend_per_decade / mean_extent:+.1f}% of the mean per decade)")
