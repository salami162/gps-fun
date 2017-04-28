from itertools import izip

import numpy as np
from haversine import haversine

# Result of haversine((lat+1, lng), (lat, lng)) for all combinations of lat, lng
KILOMETERS_PER_DEGREE_LATITUDE = 111.1338401207391
KM_TO_METERS = 1000
MAX_DISTANCE_WITHIN_CLUSTER_IN_METERS = 100


def find_nearby_pairs(items, radius_km):
    threshold_lat = radius_km / KILOMETERS_PER_DEGREE_LATITUDE

    sorted_items = sorted(items, key=lambda x: x[0])
    for i, item1 in enumerate(sorted_items):
        for j in xrange(i + 1, len(sorted_items)):
            item2 = sorted_items[j]

            if item2[0] - item1[0] > threshold_lat:
                # All items to the "right" of item2 will be furth than radius_km, so we can break out of the inner loop
                break

            if haversine((item1[0], item1[1]), (item2[0], item2[1]), miles=False) < radius_km:
                yield (item1, item2)


def dedupe_by_id(objects):
    """
    Deduplicate objects according to id().
    :param iter[object] objects:
    :return list[object]:
    """
    return {id(o): o for o in objects}.values()


def union_find(items, edges):
    p_to_c = {item: {item} for item in items}
    for p1, p2 in edges:
        # Find
        if p_to_c[p1] is p_to_c[p2]:
            continue

        # Get small and large set
        small, large = sorted([p_to_c[p1], p_to_c[p2]], key=len)
        large.update(small)
        for p in small:
            p_to_c[p] = large

    # p_to_c.values() contains each cluster multiple times, de-dupe it
    return dedupe_by_id(p_to_c.itervalues())


def nearest(clusters, centers):
    """
    Get the location in the input data that is closest to the centroid of each cluster.
    :param list[list[app.models.base_location.BaseLocation]] clusters:
    :param list[(float, float)] centers:
    :return list[dict]: The closest location for each of the clusters (same length as clusters_by_index).
    """
    nearest_locations = []

    for cluster, center in izip(clusters, centers):
        nearest_location = min(
            cluster,
            key=lambda loc: haversine(center, (loc[0], loc[1]))
        )
        nearest_locations.append(nearest_location)

    return [loc for loc in nearest_locations]


def calculate_centers(clusters, base_locations, weights):
    """
    Given a list of clusters, and weights for each location, find the weighted centroid of each cluster.
    :param iter[list[app.models.base_location.BaseLocation]] clusters:
    :param list[app.models.base_location.BaseLocation] base_locations:
    :param list[float] weights: weights[i] corresponds to base_locations[i]
    :return list[(float, float)]: centroids
    """
    if weights:
        loc_to_weight = dict(izip(base_locations, weights))
    else:
        loc_to_weight = {loc: 0 for loc in base_locations}

    center_list = []
    for cluster in clusters:
        lats, lngs, weights = zip(*[(l[0], l[1], loc_to_weight[l]) for l in cluster])
        total_weight = sum(weights) or 1
        center_list.append((
            np.dot(lats, weights) / total_weight,
            np.dot(lngs, weights) / total_weight,
        ))

    return center_list
