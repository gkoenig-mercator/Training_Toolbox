# Dry run without any area, period or depth: the whole dataset for this variable
whole_dataset_dry_run = copernicusmarine.subset(
    dataset_id=dataset_id,
    variables=["thetao"],
    dry_run=True,
)

print(f"Estimated file size: {whole_dataset_dry_run.file_size / 1000:.0f} GB")
print(f"That is {whole_dataset_dry_run.file_size / dry_run_response.file_size:,.0f} times larger than our Fram Strait selection")
