# Sea ice extent of every March (the data are transferred at this step)
march = select_month(sea_ice["siconc"], month=3)
march_extent = compute_sea_ice_extent(march)

# Both seasons on the same figure
plot_extent_trend(september_extent, "September")
plot_extent_trend(march_extent, "March")
plt.show()
