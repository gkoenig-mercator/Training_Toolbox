# Open the daily dataset remotely: nothing is downloaded yet
daily_sea_ice = copernicusmarine.open_dataset(
    dataset_id="cmems_mod_arc_phy_my_nextsim_P1D-m",
    dataset_part="originalGrid",
    variables=["siconc"],
)

print("Number of days:", daily_sea_ice.time.size)
print("Size if it were downloaded (GB):", round(daily_sea_ice["siconc"].nbytes / 1e9))
