from queue import PriorityQueue


def jak_dojade(G, P, d, a, b):
    n = len(G)
    Q = PriorityQueue()

    dp = [100000] * n
    p = [-1] * n

    dp[a] = 0
    Q.put((0, a, d))

    while not Q.empty():
        u = Q.get()

        if u[1] not in P:
            benzin = u[2]
        else:
            benzin = d

        for i in range(n):
            if dp[i] > dp[u[1]] + G[u[1]][i] and G[u[1]][i] != -1 and G[u[1]][i] <= benzin:
                Q.put((G[u[1]][i], i, benzin - G[u[1]][i]))
                dp[i] = dp[u[1]] + G[u[1]][i]
                p[i] = u[1]

    if p[b] == -1:
        return None
    else:
        road = read_road(p, a, b)
        return road[::-1]


def read_road(p, a, b):
    road = [b]
    while p[b] != -1:
        b = p[b]
        road.append(b)
    return road


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]

P = [0, 1, 3]

print(jak_dojade(G, P, 6, 0, 2))
