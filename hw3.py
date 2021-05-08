import json

data = input()
#data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C" , "parents": ["A"]}]'
x = json.loads(data)

def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    res = []

    while queue:
        s = queue.pop(0)
        res.append(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return res

graph = {}
for dic in x:
    l = []
    for v in dic.values():
        l.append(v)
    graph[l[0]] = l[1]
graph = dict(sorted(graph.items()))

result = {}
for k in graph.keys():
    result[k] = []
keys = list(result.keys())

for (k,v) in graph.items():
    ll = []
    for i in v:
        for key in keys:
            if key==i:
                result[key].append(k)

for k in result.keys():
    print(k + ": " + str(len(bfs(result, k))))