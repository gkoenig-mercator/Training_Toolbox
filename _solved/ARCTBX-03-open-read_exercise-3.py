# Sea ice extent of every March 15th (the data are transferred at this step)
march = select_day_each_year(sea_ice["ice_conc"], month=3, day=15)
march_extent = compute_sea_ice_extent(march)

# Both seasons on the same figure
plot_extent_trend(september_extent, "September")
plot_extent_trend(march_extent, "March")
plt.show()
