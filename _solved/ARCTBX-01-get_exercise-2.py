# The dry run of exercise 1 is repeated here, so that this solution works on its own
reprocessed_dataset = copernicusmarine.get(
    dataset_id="cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m",
    dry_run=True,
)

first_file = reprocessed_dataset.files[0]
last_file = reprocessed_dataset.files[-1]

print(f"First file: {first_file.filename}")
print(f"Last file:  {last_file.filename}")
print(f"Size of one file: {first_file.file_size:.1f} MB")
