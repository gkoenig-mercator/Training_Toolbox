# Open the daily dataset remotely: nothing is downloaded yet
daily_sea_ice = copernicusmarine.open_dataset(
    dataset_id="cmems_mod_arc_phy_my_nextsim_P1D-m",
    dataset_part="originalGrid",
    variables=["siconc"],
)

print(f"Number of days: {daily_sea_ice.time.size}")
print(f"Size if it were downloaded: {daily_sea_ice['siconc'].nbytes / 1e9:.0f} GB")
print(f"That is {daily_sea_ice['siconc'].nbytes / sea_ice['siconc'].nbytes:.0f} times more than the monthly dataset")
