graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex) 
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex) 
            stack.extend(reversed(graph[vertex]))
print("DFS (Recursive):")
dfs_recursive(graph, 'A')

print("\nDFS (Iterative):")
dfs_iterative(graph, 'A')
