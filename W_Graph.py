class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        self.nodes.append(node)
    def connect(self, node1, node2, weight):
        if type(weight).__name__ != ('int' or 'float'):
            raise Exception('The weight should be int or float not %s' % str(type(weight).__name__))

        if node1 and node2 in self.nodes:
            if node1 in self.edges:
                self.edges[node1].update({node2:weight})
            else:
                self.edges[node1] = {node2:weight}

            if node2 in self.edges:
                self.edges[node2].update({node1:weight})
            else:
                self.edges[node2] = {node1:weight}
        else:
            raise Exception("Check if any of these node is in graph")
    def weight(self,node1,node2):
        if self.isconnected(node1,node2):
            return self.edges[node1][node2]
        raise Exception("Check if any of these node is in graph")
    def isconnected(self, node1, node2) -> bool:
        if node1 and node2 in self.edges:
            all_node = self.edges[node1]
            if node2 in all_node:
                return True
        return False


class Node:
    def __init__(self,val):
        self.val=val
        self.parent:Node=None
    def __lt__(self, other):
        return other<self.val