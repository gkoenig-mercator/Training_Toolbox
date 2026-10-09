# First and last March of the dataset
mid_march_1979 = sea_ice["ice_conc"].sel(time="1979-03-15", method="nearest")
plot_arctic_map(
    mid_march_1979,
    "Sea ice concentration - March 1979",
    cmap="Blues_r", vmin=0, vmax=1,
    cbar_kwargs={"label": "Sea ice concentration"},
)
plt.show()

mid_march_2020 = sea_ice["ice_conc"].sel(time="2020-03-15", method="nearest")

plot_arctic_map(
    last_march_2020,
    "Sea ice concentration - March 2020",
    cmap="Blues_r", vmin=0, vmax=1,
    cbar_kwargs={"label": "Sea ice concentration"},
)
plt.show()
