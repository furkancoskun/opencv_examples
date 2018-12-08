import weightedstats as ws

my_data = [1, 2, 3, 4, 5]
my_weights = [10, 1, 1, 1, 9]

# Ordinary (unweighted) mean and median
print (ws.mean(my_data))    # equivalent to ws.weighted_mean(my_data)
ws.median(my_data)  # equivalent to ws.weighted_median(my_data)

# Weighted mean and median
ws.weighted_mean(my_data, weights=my_weights)
ws.weighted_median(my_data, weights=my_weights)

# Special weighted mean and median functions for use with numpy arrays
ws.numpy_weighted_mean(my_data, weights=my_weights)
ws.numpy_weighted_median(my_data, weights=my_weights)
