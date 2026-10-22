# Open the continuation of the record remotely: nothing is downloaded yet
interim_sea_ice = copernicusmarine.open_dataset(
    dataset_id="OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS",
    variables=["ice_conc"],
)

print("Number of days:", interim_sea_ice.time.size)
print("Last day:", interim_sea_ice.time.values[-1])
