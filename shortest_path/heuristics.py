import math

def zero(a,b) -> float:
    return 0.0
def manhattan(a,b) -> float:
    (r1,c1), (r2,c2) = a,b
    return abs(r1-r2) + abs(c1-c2)
def euclidean(a,b) -> float:
    (r1,c1), (r2,c2) = a,b
    return math.sqrt((r1-r2)**2 + (c1-c2)**2) 