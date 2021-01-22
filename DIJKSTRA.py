from W_Graph import Graph, Node
from heapq import *

city = Graph()
city.addNode("A")
city.addNode("B")
city.addNode("C")
city.addNode("D")
city.addNode("E")
city.addNode("F")
city.connect("A", "B", 6)
city.connect("A", "D", 1)
city.connect("A", "E", 3)
city.connect("D", "B", 3)
city.connect("D", "E", 1)
city.connect("B", "E", 5)
city.connect("B", "F", 1)
city.connect("E", "C", 4)
city.connect("C", "F", 2)


def dijkstra(graph: Graph, f, t):
    mins = {f: 0}
    q = [(0, Node(f))]
    seen=set()
    while q:
        cost, v1 = heappop(q)
        if v1.val == t:
            return v1
        if v1.val not in seen:
            seen.add(v1.val)
        for v2 in graph.edges[v1.val]:
            prev = mins.get(v2, float('inf'))
            next = cost + graph.edges[v1.val][v2]
            if next < prev and v2 not in seen:
                mins[v2] = next
                v2 = Node(v2)
                v2.parent = v1
                heappush(q, (next, v2))

    return float("inf")


if __name__ == "__main__":
    d = dijkstra(city, "A", "F")
    path=[]
    while d:
        path.append(d.val)
        d=d.parent
    while path:
        if len(path)>1:
            print(path.pop(), end=" --> ")
        else:
            print(path.pop(),end=" ")

