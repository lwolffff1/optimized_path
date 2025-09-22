from shortest_path.graph import Grid
from shortest_path.algorithms.astar import astar_grid
from shortest_path.heuristics import manhattan

def test_grid():
    lines = ["...", "...", "..."]
    grid = Grid(lines)
    dist, path = astar_grid(grid, (0,0), (2,2), manhattan)
    assert dist == 4
    assert path[0] == (0,0) and path[-1] == (2,2)