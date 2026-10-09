# Get the salinity file of exercise 3 (it is not downloaded again if it is already there)
salinity_response = copernicusmarine.subset(
    dataset_id=dataset_id,
    variables=["so"],
    minimum_longitude=minimum_longitude,
    maximum_longitude=maximum_longitude,
    minimum_latitude=minimum_latitude,
    maximum_latitude=maximum_latitude,
    start_datetime=start_date,
    end_datetime=end_date,
    minimum_depth=minimum_depth,
    maximum_depth=maximum_depth,
    output_directory=data_directory,
    output_filename="fram_strait_salinity_2024-08.nc",
    skip_existing=True,
)
salinity = xr.open_dataset(salinity_response.file_path)["so"].isel(time=0).sortby("depth")
salinity_section = salinity.sel(latitude=79, method="nearest")

fig, ax = plt.subplots(figsize=(12, 5))
salinity_section.plot(
    ax=ax, y="depth", yincrease=False,
    cmap="viridis", vmin=32, vmax=35.2,
    cbar_kwargs={"label": "Salinity"},
)
salinity_section.plot.contour(ax=ax, y="depth", yincrease=False, levels=[34.9], colors="black")
ax.set_title("Salinity across the Fram Strait at 79°N - August 2024 (black line: 34.9)")
plt.show()
