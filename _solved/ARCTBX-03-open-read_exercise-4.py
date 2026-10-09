# Number of different platforms, and of measurements, for each type of platform
platforms_per_type = temperature_data.groupby("platform_type").agg(
    number_of_platforms=("platform_id", "nunique"),
    number_of_measurements=("value", "size"),
)
print(platforms_per_type)

# Bonus: where are they? One point per platform and position
positions = temperature_data.drop_duplicates(subset=["platform_id", "longitude", "latitude"])
fig, ax = plt.subplots(figsize=(8, 6))
for platform_type, group in positions.groupby("platform_type"):
    ax.scatter(group["longitude"], group["latitude"], label=platform_type, s=20)
ax.set_xlabel("Longitude (°E)")
ax.set_ylabel("Latitude (°N)")
ax.set_title("Position of the platforms measuring temperature")
ax.legend(title="Platform type")
plt.show()
