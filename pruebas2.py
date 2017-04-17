import gmaps
import gmaps.datasets
gmaps.configure(api_key="AIzaSyARcIa_zA92juUCk25JGW9GXYzgiAhV7wo") # Your Google API key

# load a Numpy array of (latitude, longitude) pairs
locations = gmaps.datasets.load_dataset("taxi_rides")

m = gmaps.Map()
m.add_layer(gmaps.heatmap_layer(locations))
m
