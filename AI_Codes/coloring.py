# Check if it's safe to assign color c to vertex v
def is_safe(graph, color, v, c):
    """Check if color c can be assigned to vertex v."""
    for i in range(len(graph)):
        # If there is an edge and the neighbor has same color
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


# Backtracking function
def graph_coloring(graph, m, color, v):
    """Try to color the graph using at most m colors."""

    # Base case: all vertices are colored
    if v == len(graph):
        return True

    # Try all colors from 1 to m
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c  # Assign color

            if graph_coloring(graph, m, color, v + 1):
                return True

            color[v] = 0  # Backtrack

    return False


# Main function
def solve_graph_coloring(graph, m):
    """Initialize and solve the graph coloring problem."""
    color = [0] * len(graph)

    if graph_coloring(graph, m, color, 0):
        print("Solution found:")
        print(color)
    else:
        print("No solution exists")


# Adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Number of colors
m = 3

solve_graph_coloring(graph, m)