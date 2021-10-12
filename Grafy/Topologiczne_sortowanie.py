# Topologiczne sortowanie :3


def DFS_Tp(G):
    n = len(G)
    v = [-1] * n
    delete = []

    i = 0
    while i != n - 1:
        delete, v = DFSVisit_Tp(G, i, v, delete)
        while i != n - 1 and v[i] != -1:
            i += 1

    return delete[::-1]


def DFSVisit_Tp(G, u, v, delete):
    v[u] = 1
    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit_Tp(G, i, v, delete)

    delete.append(u)

    return delete, v


G = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 0]]

print(DFS_Tp(G))
graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
