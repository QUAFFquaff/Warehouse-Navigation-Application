import networkx as nx
import matplotlib.pyplot as plt
import utils.LoggerFactory as LF
logger=LF.get_logger(__name__)
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
    logger.info("start drawing png graph")
    res = [products[i-1][0] for i in range(1,len(res_ind)-1)]
    plt.figure(figsize=(9, 9))
    G = nx.DiGraph()
    G.add_node(0,label = 'Smile!', pos=(0,0))
    for p in products:
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]))

    G.add_edge(0, res[0])
    G.add_edge(res[-1],0)
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
    logger.info("draw_png_graph generate: path.png")

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
    logger.info("draw_png_dot_graph generate: path.png")
