from heapq import heappush, heappop
from typing import Dict, Tuple, Optional

def reconstruct(prev: Dict, s, t):
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        if cur == s: break
        cur = prev.get(cur)
    return list(reversed(path)) if path and path[0]==s else []

def astar_grid(grid, start: tuple, goal: tuple, heuristic):
    g = {start: 0.0}
    f = {start: heuristic(start, goal)}
    prev = {start: None}
    pq = [(f[start], start)]
    closed = set()

    while pq:
        _, u = heappop(pq)
        if u in closed: 
            continue
        closed.add(u)
        if u == goal:
            return g[u], reconstruct(prev, start, goal)

        for v in grid.neighbors(*u):
            tentative = g[u] + grid.dist(u, v)
            if tentative < g.get(v, float('inf')):
                g[v] = tentative
                f[v] = tentative + heuristic(v, goal)
                prev[v] = u
                heappush(pq, (f[v], v))

    return float('inf'), []