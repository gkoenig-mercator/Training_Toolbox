# March sea ice extent: area of the cells with at least 15% of ice
march = sea_ice["siconc"].sel(time=sea_ice.time.dt.month == 3)
march_extent = (cell_area.where(march >= 0.15).sum(dim=["y", "x"]) / 1e6).compute()

march_years = march_extent.time.dt.year.values
march_slope, march_intercept = np.polyfit(march_years, march_extent.values, 1)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(march_years, march_extent, marker="o", color="tab:blue", label="March extent")
ax.plot(march_years, march_slope * march_years + march_intercept, "--", color="tab:blue",
        label=f"Trend: {10 * march_slope:+.2f} million km² per decade")
ax.plot(years, september_extent, marker="o", color="tab:orange", label="September extent")
ax.set_xlabel("Year")
ax.set_ylabel("Sea ice extent (million km²)")
ax.set_title("Arctic sea ice extent in March and September")
ax.legend()
plt.show()

print(f"March trend:     {10 * march_slope:+.2f} million km² per decade "
      f"({100 * 10 * march_slope / float(march_extent.mean()):+.1f}% of the mean per decade)")
print(f"September trend: {10 * slope:+.2f} million km² per decade "
      f"({100 * 10 * slope / float(september_extent.mean()):+.1f}% of the mean per decade)")
