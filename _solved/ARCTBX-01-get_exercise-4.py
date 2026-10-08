# Get the file of 22 March 2025 (it is not downloaded again if it is already there)
maximum_response = copernicusmarine.get(
    dataset_id=dataset_id,
    filter="*20250322*",
    output_directory=data_directory,
    no_directories=True,
    skip_existing=True,
)
maximum_data = xr.open_dataset(maximum_response.files[0].file_path)

# Two maps side by side, with the same colour scales as the September maps
fig, axes = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={"projection": ccrs.NorthPolarStereo()})

plot_arctic_map(
    maximum_data["analysed_st"].isel(time=0) - 273.15,
    "Surface temperature - 22 March 2025",
    ax=axes[0],
    cmap="RdBu_r", vmin=-40, vmax=10,
    cbar_kwargs={"label": "Surface temperature (°C)", "shrink": 0.7},
)
plot_arctic_map(
    maximum_data["sea_ice_fraction"].isel(time=0),
    "Sea ice fraction - 22 March 2025",
    ax=axes[1],
    cmap="Blues_r", vmin=0, vmax=1,
    cbar_kwargs={"label": "Sea ice fraction", "shrink": 0.7},
)
plt.show()
