# Same request as for the temperature, with the variable PSAL
salinity_data = copernicusmarine.read_dataframe(
    dataset_id=insitu_dataset_id,
    dataset_part="history",
    variables=["PSAL"],
    minimum_longitude=12.0,
    maximum_longitude=15.5,
    minimum_latitude=77.8,
    maximum_latitude=78.4,
    minimum_depth=0,
    maximum_depth=200,
    start_datetime="2021-01-01",
    end_datetime="2023-12-31",
)

summarize_platforms(salinity_data)
