# Select the months of March, then the first and last March of the dataset
march = sea_ice["siconc"].sel(time=sea_ice.time.dt.month == 3)
first_march = march.isel(time=0)
last_march = march.isel(time=-1)

fig, axes = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={"projection": NEXTSIM_PROJECTION})
for ax, month in zip(axes, [first_march, last_march]):
    plot_nextsim_map(
        month,
        f"Sea ice concentration - {pd.Timestamp(month.time.values):%B %Y}",
        ax=ax,
        cmap="Blues_r", vmin=0, vmax=1,
        cbar_kwargs={"label": "Sea ice concentration", "shrink": 0.7},
    )
plt.show()
