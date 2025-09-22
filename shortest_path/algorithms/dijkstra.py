from heapq import heappush, heappop
from typing import Dict, Tuple, List, Optional

def _iter_neighbors(G, u):
    if hasattr(G, "neighbors"):
        return G.neighbors(u)
    if hasattr(G, "get_neighbors"):
        return G.get_neighbors(u)
    raise AttributeError("Graph object must define neighbors(u) or get_neighbors(u)")


def reconstruct(prev: Dict[str, Optional[str]], s: str, t: str):
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        if cur == s: break
        cur = prev.get(cur)
    return list(reversed(path)) if path and path[0]==s else []

def dijkstra(graph, s: str, t: str):
    dist = {s: 0.0}
    prev = {s: None}
    pq = [(0.0, s)]
    visited = set()

    while pq:
        d, u = heappop(pq)
        if u in visited: 
            continue
        visited.add(u)
        if u == t: 
            return d, reconstruct(prev, s, t)

        for v, w in graph.neighbors(u):
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                prev[v] = u
                heappush(pq, (nd, v))

    return float('inf'), []