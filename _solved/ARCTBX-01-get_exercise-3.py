# 1. Check the selection with a dry run: we expect exactly one file
maximum_dry_run = copernicusmarine.get(
    dataset_id=dataset_id,
    filter="*20250322*",
    dry_run=True,
)
print(f"Number of files selected: {maximum_dry_run.number_of_files_to_download}")

# 2. Download it
maximum_response = copernicusmarine.get(
    dataset_id=dataset_id,
    filter="*20250322*",
    output_directory=data_directory,
    no_directories=True,
    skip_existing=True,
)

maximum_file = Path(maximum_response.files[0].file_path)
print(f"File downloaded: {maximum_file}")
print(f"The file exists: {maximum_file.exists()}")
