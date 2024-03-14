import sys
import re
    
def count(graph, start, current, total):
    current += 1
    if graph.get(start,None) == None:
        if current >= 6:
            return total + 1
    else:
        for node in graph[start]:
            total = count(graph, node, current, total)
    return total

def build_graph(data):
    nodes = data.split(" ")
    print(nodes)
    graph = {}
    for node in nodes:
        graph[re.split(":|,", node)[0]] = set(re.split(":|,", node)[1:])
    return graph

if __name__ == '__main__':
    data = input()
    print(count(build_graph(data), '1', 0, 0))