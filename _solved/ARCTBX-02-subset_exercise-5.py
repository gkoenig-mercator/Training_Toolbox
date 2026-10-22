# Get the salinity file of exercise 4 (it is not downloaded again if it is already there)
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
salinity = xr.open_dataset(salinity_response.file_path)

plot_depth_section(
    salinity["so"],
    latitude=79,
    title="Salinity across the Fram Strait at 79°N - August 2024 (black line: 34.9)",
    cbar_label="Salinity",
    cmap="viridis",
    vmin=32,
    vmax=35.2,
    contour_level=34.9,
)
