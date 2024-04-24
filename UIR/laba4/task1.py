from collections import deque


graph = {'S': ["A", "B"],
    'A':  ["S", "C", "F"],
    'B': ["S", "C", "D"],
    'C': ["A", "B"],
    'D': ["B", "F"],
    'F': ["D", "A"]}

def bfs(start, goal, graph):
    visited = set() #посещённые 
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft() #извлечение узла и соответствующего ему пути из кортежа в начале очереди
        if node == goal:
            return path  #если это то что надо, то возвращает путь
        if node not in visited: #если не посещённая вершина
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor])) #узел-сосед и путь до него
    return None 

start = 'S'
goal = 'F'
path = bfs(start, goal, graph)

if path:
    print(f"Path from {start} to {goal}: {' >> '.join(path)}")  # найденный путь в виде строки с использованием стрелок ">>"
else:
    print(f"No path found from {start} to {goal}")

