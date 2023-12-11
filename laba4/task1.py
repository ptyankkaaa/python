from collections import deque


graph = {'S': ["A", "B"],
    'A':  ["S", "C", "F"],
    'B': ["S", "C", "D"],
    'C': ["A", "B"],
    'D': ["B", "F"],
    'F': ["D", "A"]}

def bfs(start, goal, graph):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None

start = 'S'
goal = 'F'
path = bfs(start, goal, graph)

if path:
    print(f"Path from {start} to {goal}: {' >> '.join(path)}")
else:
    print(f"No path found from {start} to {goal}")

