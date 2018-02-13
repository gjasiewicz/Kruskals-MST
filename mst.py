from euclidean_graph import all_edges_sorted, random_points
import union_find as uf


def mst(points):
    """Kruskal's algorithm (minimal spanning tree).
    It finds a subset of the edges that forms a tree
    that includes every vertex,
    where the total weight of all the edges in the tree is minimized.
    type points: numpy array, 2D-coordinates
    rtypes: lists of tuples and integer
    We also return number of edges,
    on which we have to look before we get MST
    and list of edges not used."""
    E = all_edges_sorted(points)
    n = len(points)
    boss = uf.FindUnion(n)
    mst_edges = []
    not_edges = []
    counter = 0
    for v1, v2 in E:
        if len(mst_edges) == n-1:
            return mst_edges, counter, not_edges
        counter += 1
        if boss.find_boss(v1) != boss.find_boss(v2):
            boss.union_boss(v1, v2)
            mst_edges.append((v1, v2))
        else:
            not_edges.append((v1, v2))
    return mst_edges, counter, not_edges
            
            
        
