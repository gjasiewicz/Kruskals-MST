import math
from euclidean_graph import *
from visual import *
from mst import *


def tests():
    test_draw_points()
    test_draw_edge()
    test_draw_edges()
    test_all_edges_sorted()
    test_mst()
    test_mst_with_edges_not_used()


def test_draw_points():
    p = random_points(5)
    draw_points(p)


def test_draw_edge():
    p1, p2 = random_points(2)
    draw_edge(p1, p2)


def test_draw_edges():
    p = random_points(6)
    E_indices = [(0, 1), (1, 2), (3, 4)]
    draw_points(p)
    draw_edges(p, E_indices)


def test_all_edges_sorted():
    p = random_points(6)
    draw_points(p)
    edges_indices = all_edges_sorted(p)
    draw_edges(p, edges_indices)


def test_mst():
    p = random_points(100)
    draw_points(p)
    mst_edges, c, not_edges = mst(p)
    draw_edges(p, mst_edges)


def test_mst_with_edges_not_used():
    p = random_points(10)
    draw_points(p)
    mst_edges, c, not_edges = mst(p)
    draw_edges(p, mst_edges, "blue", False)
    draw_edges(p, not_edges, "red", False)
    plt.title("Blue - MST edges, Red - Not used edges")
    plt.savefig("mst_with_edges_not_used10")



##if __name__ == "__main__":
##    tests()
##    plt.show()
