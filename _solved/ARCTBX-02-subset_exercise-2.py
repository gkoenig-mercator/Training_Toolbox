# Same request as for the Fram Strait, but for the Bering Strait
bering_strait_temperature = copernicusmarine.subset(
    dataset_id="cmems_mod_arc_phy_my_topaz4_P1M",
    variables=["thetao"],
    minimum_longitude=-177,
    maximum_longitude=-162,
    minimum_latitude=59,
    maximum_latitude=71,
    start_datetime="2024-08-01T00:00:00",
    end_datetime="2024-09-01T00:00:00",
    minimum_depth=0,
    maximum_depth=1000,
    dry_run=True,
)

print(f"Estimated file size: {bering_strait_temperature.file_size:.1f} MB")
print(f"Data read on the server to build it: {bering_strait_temperature.data_transfer_size:.1f} MB")
