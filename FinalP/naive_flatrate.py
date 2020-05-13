"""Summary
"""
from lib_randomgraph import RandomGraph

def main():
    """Summary
    """
    graph = RandomGraph('Gnp', 4, edge_spec=.5, seed=42)

    print(graph)
    budget = 100
    flatrate = 4
    nodes, value = naive_flatrate(graph, budget, flatrate)
    print('selected nodes ', nodes)
    print('total value    ', value)

def naive_flatrate(graph, budget, flatrate):
    """No complementarities, pays same flatrate amount to all landowners in decreaseing order of property value, landowners accept if flatrate above their (hidden) cost
    
    Args:
        graph (TYPE): Description
        budget (TYPE): Description
    """
    value = 0
    cost = 0
    nodes = set()

    node_values = list(enumerate(graph.node_weights))
    node_values_sorted = sorted(node_values, key = lambda x: x[1][1], reverse=True)

    for node in node_values_sorted:
        if cost + flatrate > budget:
            break

        node_id = node[0]
        node_cost = node[1][0]
        node_value = node[1][1]

        if node_cost <= flatrate:
            nodes.add(node_id)
            cost += flatrate
            value += node_value


    # complementarity values
    comp = 0
    for node in nodes:
        for adjacent in graph.graph[node]:
            if adjacent[0] in nodes:
                comp += adjacent[1]
    comp /= 2 # counted each edge twice
    value += comp

    return (nodes, value)

if __name__ == '__main__':
    main()
