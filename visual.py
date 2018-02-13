import numpy as np
import matplotlib.pyplot as plt


def draw_points(points):
    """type points: numpy array, shape(number_of_points, 2)
    rtype: plot"""
    for point in points:
        plt.scatter([point[0]], [point[1]])


def draw_edge(p1, p2, color=None, show_axes=None):
    """type p1, p2: numpy array, 2D-coordinates
    rtype: plot"""
    plt.plot((p1[0], p2[0]), (p1[1], p2[1]), color=color)
    if show_axes is False:
        cur_axes = plt.gca()
        cur_axes.axes.get_xaxis().set_visible(False)
        cur_axes.axes.get_yaxis().set_visible(False)


def draw_edges(points, E_indices, color=None, show_axes=None):
    """type points: numpy array, shape(number_of_points, 2)
    type E_indices: list of tuples,
    tuple indicate indices of points to draw edge between them
    rtype: plot"""
    i = 0
    for e in E_indices:
        p1, p2 = points[e[0]], points[e[1]]
        draw_edge(p1, p2, color=color, show_axes=show_axes)
        i += 1
        #plt.savefig("{}".format(i))


