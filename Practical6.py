import numpy as np

def OBST(p, q, key):
    n = len(key)
    e = np.zeros((n + 2, n + 1))
    w = np.zeros((n + 2, n + 1))
    root = np.zeros((n + 1, n + 1), dtype=int)

    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = float("inf")
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

p = np.array([0.1, 0.2, 0.4, 0.3])
q = np.array([0.05, 0.1, 0.05, 0.05, 0.1])
key = np.array([10, 20, 30, 40])

value, root = OBST(p, q, key)

print(np.round(value, 2))
print("The value of expected cost graph: ", np.round(value[1, 4], 4))
