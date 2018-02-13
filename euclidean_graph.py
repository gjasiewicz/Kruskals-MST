import numpy as np


def random_points(n):
    """type n: integer, number of points
        rtype: numpy array, shape(n, 2)"""
    return np.random.random((n, 2))


def distance(p1, p2):
    """type p1, p2: numpy array, 2D-coordinates
        rtype: float"""
    return np.linalg.norm(p1 - p2)


def all_edges_sorted(points):
    """We get a list of all possible edges between points,
    sorted by distance between them.
    Each edge is represented by tuple of indices of corresponding points
    (smaller index first)
    type points: numpy array, 2D-coordinates
    rtype: list of tuples"""

    edges_indices = []
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points[i+1:], i+1):
            edges_indices.append((distance(point1, point2), (i, j)))
    edges_indices.sort()
    return [edge for dist, edge in edges_indices]


