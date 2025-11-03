def hamiltonian(position, path, graph, n, labels):
    if position == n:
        if graph[path[n - 1]][path[0]] == 1:
            cycle = [labels[v - 1] for v in path]
            print("Hamiltonian Cycle:", " → ".join(cycle))
        return

    for vertex in range(2, n + 1):
        if graph[path[position - 1]][vertex] == 1 and vertex not in path[:position]:
            path[position] = vertex
            hamiltonian(position + 1, path, graph, n, labels)
            path[position] = 0


def next_level(graph, n, labels):
    path = [0] * n
    path[0] = 1
    hamiltonian(1, path, graph, n, labels)


# Example usage
graph = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0]
]

labels = ['A', 'B', 'C', 'D', 'E']
n = 5

next_level(graph, n, labels)
