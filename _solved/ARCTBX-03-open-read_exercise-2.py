# Select the months of March, then the first and last March of the dataset
first_march= sea_ice["siconc"].sel(time="1993-03-01")

plot_nextsim_map(
    first_march,
    "Sea ice concentration - March 1993",
    cmap="Blues_r", vmin=0, vmax=1,
    cbar_kwargs={"label": "Sea ice concentration"},
)
plt.show()

last_march= sea_ice["siconc"].sel(time="2025-03-01")

plot_nextsim_map(
    last_march,
    "Sea ice concentration - March 2025",
    cmap="Blues_r", vmin=0, vmax=1,
    cbar_kwargs={"label": "Sea ice concentration"},
)
plt.show()
