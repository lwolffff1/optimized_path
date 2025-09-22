import time
from shortest_path.graph import Grid
from shortest_path.heuristics import zero, manhattan
from shortest_path.algorithms.astar import astar_grid

def make_open_grid(n):
    line = "." * n
    return Grid([line for _ in range(n)])

if __name__ == "__main__":
    g = make_open_grid(200)
    s, t = (0,0), (199,199)

    for name, h in [("zero (Dijkstra)", zero), ("A* Manhattan", manhattan)]:
        t0 = time.time()
        dist, _ = astar_grid(g, s, t, h)
        dt = time.time() - t0
        print(f"{name:15s}: dist={dist}, time={dt:.3f}s")