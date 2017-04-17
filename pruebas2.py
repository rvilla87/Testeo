import gmaps
import gmaps.datasets
import secret

gmaps.configure(api_key=secret.GMAPS_KEY) # Your Google API key

# load a Numpy array of (latitude, longitude) pairs
locations = gmaps.datasets.load_dataset("taxi_rides")

m = gmaps.Map()
m.add_layer(gmaps.heatmap_layer(locations))
m
