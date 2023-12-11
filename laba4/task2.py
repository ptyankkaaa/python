from collections import deque


graph = {'cab': ["car", "cat"],
    'car':  ["cat", "bar"],
    'cat': ["mat", "bat"],
    'mat': ["bat"],
    'bar': ["bat"]}

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

start = 'cab'
goal = 'bat'
path = bfs(start, goal, graph)

if path:
    print(f"Path from {start} to {goal}: {' >> '.join(path)}")
else:
    print(f"No path found from {start} to {goal}")
