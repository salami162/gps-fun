import numpy as np
from colorutils import Color


def visualize_as_geojson(data, labels=None, centroids=None, sample_scale=10):
    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

    num_colors = len(data)
    if centroids:
        num_colors = len(centroids)

    colors = np.random.randint(255, size=(num_colors, 3))
    colors = [Color(tuple(i)).hex for i in colors]

    for i in np.random.choice(len(data), len(data) / sample_scale, replace=False):
        if labels:
            marker_color = colors[labels[i]]
        else:
            marker_color = colors[i]
        geojson['features'].append({
            'type': 'Feature',
            'properties': {
                'marker-color': marker_color,
                'icon': 'marker'
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [float(data[i][1]), float(data[i][0])]
            }
        })

    if centroids:
        geojson = generate_centeroid_marker(centroids, colors, geojson)

    return geojson


def generate_centeroid_marker(centroids, colors, geojson):
    for i in range(len(centroids)):
        # Add a larger icon for centroids
        geojson['features'].append({
            'type': 'Feature',
            'properties': {'marker-color': colors[i], 'marker-size': 'large', 'marker-symbol': str(i)},
            'geometry': {
                'type': 'Point',
                'coordinates': [float(centroids[i][1]), float(centroids[i][0])]
            }
        })
    return geojson
