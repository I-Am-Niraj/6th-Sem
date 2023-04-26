"""
graph = {
  'A' : ['B','D', 'F'],
  'B' : ['C'],
  'D' : ['E', 'F']
}
"""

n = int(input("Enter the number of nodes in graph: "))
graph = {}

for i in range(n):
  key = input("Enter key for node: ")
  value = list(map(str, input("Enter values separated by space: ").split()))
  graph[key] = value

print("Graph: ", graph)

visited = []

queue = []

visited.append('0')
queue.append('0')

while queue:
    s = queue.pop(0) 
    print (s, end = " ")
    
    for frontier in graph[s]:
        if frontier not in visited:
            visited.append(frontier)
            queue.append(frontier)