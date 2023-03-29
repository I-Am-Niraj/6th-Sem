from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, weights):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in came_from:
                priority = weights[neighbor] 
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    return came_from

graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("Enter the node: ")
    neighbors = input("Enter the neighbors separated by spaces: ")
    graph[node] = neighbors.split()

weights = {}
for node in graph:
    weight = int(input("Enter the weight of node {}: ".format(node)))
    weights[node] = weight

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

came_from = greedy_best_first_search(graph, start, goal, weights)

path = []
current = goal
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start)
path.reverse()

print("Shortest path:", path)