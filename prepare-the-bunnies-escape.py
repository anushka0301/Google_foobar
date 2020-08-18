def solution(m):
    w, h = len(m[0]), len(m)
    minimum = 401
    for m1 in maps_one(m):
        minimum = min(path(m1, w, h), minimum)
        if minimum == w + h - 1:
            return minimum
    return minimum

def path(m, w, h):
    d = {1: {(0,0)}}
    length = 2
    while length < 401 and d[length-1]:
        fringe = set()
        for x in d[length-1]:
            expand = {y for y in neighbors(x,m) if not any(y in visited for visited in d.values())}
            fringe = fringe | expand
            
        if (h-1, w-1) in fringe:
            return length

        d[length] = fringe
        length += 1
    return 401
        
def neighbors(x, m):
    i, j = x
    w, h = len(m[0]), len(m)
    candidates = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
    neighbors = set()
    for y in candidates:
        i, j = y
        if i>=0 and i<h and j>=0 and j<w and m[i][j] == 0:
            neighbors.add(y)
    return neighbors

def maps_one(m):
    yield m
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]:
                copy = [[col for col in row] for row in m]
                copy[i][j] = 0
                yield copy