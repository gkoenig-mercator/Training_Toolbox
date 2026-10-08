# Dry run on the reprocessed (multi-year) product: nothing is downloaded
reprocessed_dataset = copernicusmarine.get(
    dataset_id="cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m",
    dry_run=True,
)

print(f"Number of files: {reprocessed_dataset.number_of_files_to_download}")
print(f"Total size: {reprocessed_dataset.total_size / 1000:.0f} GB")
