from shortest_path.graph import Graph
from shortest_path.algorithms.dijkstra import dijkstra

def test_simple():
    adj = {"A":[("B",1),("C",5)], "B":[("C",1)], "C":[]}
    g = Graph(adj)
    dist, path = dijkstra(g, "A", "C")
    assert dist == 2
    assert path == ["A","B","C"]