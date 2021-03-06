# Topologiczne sortowanie :3


def DFS_Tp(G):
    n = len(G)
    v = [-1] * n
    delete = []

    for i in range(n):
        if v[i] == -1:
            DFSVisit_Tp(G, i, v, delete)

    return delete[::-1]


def DFSVisit_Tp(G, u, v, delete):
    n = len(G)
    v[u] = 1
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit_Tp(G, i, v, delete)

    delete.append(u)



graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

G = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 0]]
# [0, 2, 1, 3, 7, 4, 5, 9, 6, 8]
print(DFS_Tp(graph))
graph1 = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
