
def brute_force(x_matrix,y_matrix,d_matrix,source,target):
    '''

    :param x_matrix: x difference
    :param y_matrix: y-dimensional difference
    :param d_matrix: x+y
    :param source: start point
    :param target: target point, usually source and target are the same
    :return: result list
    '''
    res = []

    return res


import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]

    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis

def draw_png_graph(products,res_ind):
    res = [products[i][0] for i in res_ind]
    plt.figure(figsize=(9, 9))
    G = nx.DiGraph()
    for p in products:
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]))
    for i in range(1,len(res)):
        G.add_edge(res[i-1],res[i])
    pos = nx.get_node_attributes(G,'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos=pos,  node_size=500, labels=node_labels, font='bond',
            arrowstyle='->', arrows=True,
            arrowsize=30, edge_color='red',
            width=1, directed=True
            )
    plt.savefig("data/path/path.png")
    print("generate: path.png")
    pass

def draw_png_dot_graph(products):
    plt.figure(figsize=(9, 9))
    G = nx.DiGraph()
    for p in products:
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]))
    pos = nx.get_node_attributes(G,'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos=pos,  node_size=500, labels=node_labels, font='bond',
            arrowstyle='->', arrows=True,
            arrowsize=30, edge_color='red',
            width=1, directed=True
            )
    plt.savefig("data/path/dot.png")
    print("generate: dot.png")
    pass

products = [[1,1,1],[2,2,4],[3,2,1]]
draw_png_dot_graph(products)
res = [1,2,3,1]
draw_png_graph(products,res)