# The second most common depth of the same mooring
second_depth = good_data["depth"].round().value_counts().index[1]
second_sensor = good_data[good_data["depth"].round() == second_depth]
second_monthly = second_sensor.set_index("time")["value"].sort_index().resample("MS").mean()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_temperature.index, monthly_temperature, marker="o", label=f"{sensor_depth:.0f} m")
ax.plot(second_monthly.index, second_monthly, marker="o", label=f"{second_depth:.0f} m")
ax.set_ylabel("Monthly mean temperature (°C)")
ax.set_title(f"Platform {chosen_platform}: monthly mean temperature at two depths")
ax.legend()
plt.show()

for depth, series in [(sensor_depth, monthly_temperature), (second_depth, second_monthly)]:
    print(f"{depth:.0f} m: seasonal range {series.max() - series.min():.1f}°C "
          f"(warmest month: {series.idxmax():%B %Y}, coldest: {series.idxmin():%B %Y})")
