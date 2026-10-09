# Deeper layer, where the Atlantic Water flows
deep_data = select_depth_layer(good_data, minimum_depth=50, maximum_depth=200)
deep_monthly = monthly_mean(deep_data)

# Both layers on the same figure
plot_monthly_temperature(surface_monthly, "Surface (0-10 m)")
plot_monthly_temperature(deep_monthly, "Deep layer (50-200 m)")
plt.show()
