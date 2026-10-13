# Same area, period and depths as the temperature, but for the salinity "so"
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

salinity_file = Path(salinity_response.file_path)
print(f"File: {salinity_file}")
print(f"The file exists: {salinity_file.exists()}")
