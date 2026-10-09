# Same request down to 1100 m, with two different selection methods
for method in ["inside", "outside"]:
    response = copernicusmarine.subset(
        dataset_id=dataset_id,
        variables=["thetao"],
        minimum_longitude=minimum_longitude,
        maximum_longitude=maximum_longitude,
        minimum_latitude=minimum_latitude,
        maximum_latitude=maximum_latitude,
        start_datetime=start_date,
        end_datetime=end_date,
        minimum_depth=0,
        maximum_depth=1100,
        coordinates_selection_method=method,
        dry_run=True,
    )
    for extent in response.coordinates_extent:
        if extent.coordinate_id == "depth":
            print(f"{method:<8} depth from {extent.minimum} to {extent.maximum} {extent.unit}")
