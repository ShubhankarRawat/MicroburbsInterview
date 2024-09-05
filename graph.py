# Import required libraries
import folium
from folium.plugins import MarkerCluster
from geopy.distance import geodesic

# Sample coordinates for points (replace these with actual coordinates)
points = [
    {"name": "Point 1", "coordinates": (-37.814, 144.96332)},  # Melbourne, AU
    {"name": "Point 2", "coordinates": (-37.820, 144.950)},   # Nearby point
    {"name": "Point 3", "coordinates": (-37.810, 144.970)},
    {"name": "Point 4", "coordinates": (-37.825, 144.980)},
    {"name": "Point 5", "coordinates": (-37.800, 144.990)},
]

# Create a map centered around the average location of the points
m = folium.Map(location=[-37.814, 144.96332], zoom_start=13)

# Add markers and lines between points
for point in points:
    folium.Marker(
        location=point["coordinates"],
        popup=point["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Draw lines between points and add distance labels
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1, p2 = points[i]["coordinates"], points[j]["coordinates"]
        distance = geodesic(p1, p2).km
        folium.PolyLine([p1, p2], color="blue", weight=1, opacity=0.5).add_to(m)
        midpoint = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        folium.Marker(
            location=midpoint,
            icon=folium.DivIcon(html=f"<div style='font-size: 12pt; color : red'>{distance:.1f} km</div>")
        ).add_to(m)

# Save the map to an HTML file
m.save("interactive_map.html")
