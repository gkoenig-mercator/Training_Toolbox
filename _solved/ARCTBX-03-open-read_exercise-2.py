# Two empty maps, side by side
ax_left, ax_right = create_two_arctic_maps()

# Left: March 1979
march_1979 = sea_ice["ice_conc"].sel(time="1979-03-15", method="nearest")
plot_arctic_map(
    march_1979,
    "Sea ice concentration - March 1979",
    ax=ax_left,
    step=1,
    cmap="Blues_r", vmin=0, vmax=100,
    cbar_kwargs={"label": "Sea ice concentration (%)"},
)

# Right: March 2020
march_2020 = sea_ice["ice_conc"].sel(time="2020-03-15", method="nearest")
plot_arctic_map(
    march_2020,
    "Sea ice concentration - March 2020",
    ax=ax_right,
    step=1,
    cmap="Blues_r", vmin=0, vmax=100,
    cbar_kwargs={"label": "Sea ice concentration (%)"},
)

plt.show()
