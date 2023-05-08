import pytest
from A_estrela import astar

BEGIN = '6'
END = '13'

@pytest.fixture
def graph():
    graph_data = []
    with open('grafo.txt', 'r') as f:
        for line in f:
            a, b, weight = line.strip().split(' ')
            graph_data.append((a, b, float(weight)))
    return graph_data

@pytest.fixture
def heuristic():
    heuristic_data = {}
    with open('heuristica.txt', 'r') as f:
        for line in f:
            node1, node2, h = line.strip().split(' ')
            if node2 == END:
                heuristic_data[node1] = float(h)
    return heuristic_data

def test_astar(graph, heuristic):
    def neighbors_fn(node1):
        neighbors = []
        for a, b, _ in graph:
            if a == node1:
                neighbors.append(b)
            elif b == node1:
                neighbors.append(a)
        return neighbors
    
    with open('resultado.txt', 'w') as f:
        s= astar(BEGIN, END, neighbors_fn, heuristic.get)
        f.write(str(s))
        
    assert astar(BEGIN, END, neighbors_fn, heuristic.get) == ['6', '5', '4', '13']
