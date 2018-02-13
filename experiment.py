import math
import numpy as np
import matplotlib.pyplot as plt
from euclidean_graph import random_points
from mst import mst


def expected_edges_counter(nr_of_points):
    nr_of_test = int(math.sqrt(nr_of_points))
    C = []
    for i in range(nr_of_test):
        points = random_points(nr_of_points)
        e, c, ne = mst(points)
        C.append(c)
    return sum(C)*1.0/nr_of_test


def mst_edges_counter_plot(size_points, size_step, save_plot=None):
    X_data = [int(x) for x in np.linspace(1, size_points, size_step)]
    Y_data2 = [x * math.log(x) for x in X_data]
    Y_data = []
    for nr_of_points in X_data:
        expected_counter = expected_edges_counter(nr_of_points)
        Y_data.append(expected_counter)
    plt.xlabel('Number of nodes in the tree')
    plt.ylabel('Number of edges')
    plt.title('Minimal number of edges to get MST (expected value)')
    plt.plot(X_data, Y_data, marker='o', linestyle='-', label='Expected number of edges')
    plt.plot(X_data, Y_data2, label='n*log(n)')
    plt.legend()
    if save_plot:
        plt.savefig("{}".format(size_points))

