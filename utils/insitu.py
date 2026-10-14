"""Helpers to explore in situ observations returned by copernicusmarine.read_dataframe."""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

# Two-letter codes used by the Copernicus Marine In Situ TAC for the types of platforms
PLATFORM_TYPES = {
    "BO": "Bottle samples",
    "CT": "CTD profiles",
    "DB": "Drifting buoys",
    "FB": "FerryBox",
    "GL": "Gliders",
    "ML": "Mini loggers",
    "MO": "Moorings",
    "PF": "Profiling floats (Argo)",
    "SM": "Sea mammals",
    "TS": "Thermosalinographs",
    "XB": "XBT profiles",
}


def summarize_platforms(table):
    """Count the platforms and the measurements for each type of platform."""
    summary = table.groupby("platform_type").agg(
        platforms=("platform_id", "nunique"),
        measurements=("value", "size"),
    )
    summary.insert(0, "description", [PLATFORM_TYPES.get(code, "") for code in summary.index])
    return summary.sort_values("measurements", ascending=False)


def plot_platform_positions(table, title="Where the measurements were made",
                            bbox=[8, 20, 76.8, 79.6]):
    """Map the positions of the measurements, with one colour per type of platform.

    `bbox` is the area shown on the map, as [min longitude, max longitude,
    min latitude, max latitude]. The default shows the west coast of Spitsbergen.
    """
    positions = table.drop_duplicates(subset=["platform_id", "longitude", "latitude"])

    projection = ccrs.NorthPolarStereo(central_longitude=(bbox[0] + bbox[1]) / 2)
    _, ax = plt.subplots(figsize=(8, 8), layout="constrained", subplot_kw={"projection": projection})
    ax.set_extent(bbox, crs=ccrs.PlateCarree())
    for platform_type, group in positions.groupby("platform_type"):
        description = PLATFORM_TYPES.get(platform_type, platform_type)
        ax.scatter(group["longitude"], group["latitude"], s=12, label=description,
                   transform=ccrs.PlateCarree(), zorder=3)

    ax.add_feature(cfeature.LAND.with_scale("10m"), facecolor="lightgrey")
    ax.coastlines("10m", linewidth=0.5)
    ax.gridlines(draw_labels={"bottom": "x", "left": "y"}, rotate_labels=False,
                 linestyle=":", linewidth=0.5)
    ax.legend(loc="upper left")
    ax.set_title(title)
    return ax


def keep_good_data(table):
    """Keep only the measurements flagged as good (quality flag 1)."""
    good = table[table["value_qc"] == 1]
    print(f"Good data kept: {len(good)} of {len(table)} measurements")
    return good


def select_depth_layer(table, minimum_depth, maximum_depth):
    """Keep only the measurements made between two depths (in metres)."""
    layer = table[table["depth"].between(minimum_depth, maximum_depth)]
    print(f"Measurements between {minimum_depth} and {maximum_depth} m: {len(layer)}")
    return layer


def monthly_mean(table):
    """Average all the measurements of the table month by month.

    Months without any measurement are kept, with an empty value (NaN).
    """
    values = pd.Series(table["value"].values, index=pd.to_datetime(table["time"]), name="value")
    return values.sort_index().resample("MS").mean()


def plot_monthly_temperature(monthly, label):
    """Plot a monthly time series and print its warmest and coldest months.

    Call it several times before plt.show() to draw several series on the same figure.
    """
    plt.gcf().set_size_inches(12, 5)
    plt.plot(monthly.index, monthly.values, marker="o", label=label)
    plt.ylabel("Monthly mean temperature (°C)")
    plt.title("Sea water temperature at the mouth of Isfjorden")
    plt.legend()

    print(f"{label}: warmest month {monthly.idxmax():%B %Y} ({monthly.max():.1f}°C), "
          f"coldest month {monthly.idxmin():%B %Y} ({monthly.min():.1f}°C), "
          f"seasonal range {monthly.max() - monthly.min():.1f}°C")
