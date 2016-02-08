import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from mongo.geo import query

G = nx.Graph()

city = 'Toulouse'

stations = list(query.stations(city))


def compute_distance(a, b):
    ''' Euclidian distance. '''
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 1/2


# Start by adding the nodes to the graph
for station in stations:
    name = station['_id']
    lat = station['p'][1]
    lon = station['p'][0]
    G.add_node(name, pos=(lat, lon))


# Connect the closest pairs of stations
for i, a in enumerate(stations):
    minimum = np.inf
    neighbour = None
    for j, b in enumerate(stations):
        if i != j:
            distance = compute_distance(a['p'], b['p'])
            if distance < minimum:
                minimum = distance
                neighbour = b
    G.add_edge(a['_id'], neighbour['_id'])

# Keep connecting the connected components until the graph is connected
while nx.is_connected(G) is False:
    for i, A in enumerate(nx.connected_components(G)):
        minimum = np.inf
        pair = None
        for j, B in enumerate(nx.connected_components(G)):
            if i != j:
                for a in A:
                    for b in B:
                        distance = compute_distance(G.node[a]['pos'], G.node[b]['pos'])
                        if distance < minimum:
                            minimum = distance
                            pair = [a, b]
        G.add_edge(pair[0], pair[1])

positions = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(14, 14))
nx.draw_networkx(G, positions, node_size=30, with_labels=False)
plt.savefig('{}.png'.format(city))
