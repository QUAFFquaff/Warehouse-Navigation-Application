
import networkx as nx
import matplotlib.pyplot as plt
import utils.LoggerFactory as LF
from objs.DataHandler import DataHandler
shelf = [
         [[20,0],[20,16]],

         [[18, 0], [18, 16]],
         [[16, 0], [16, 16]],
         [[14, 0], [14, 16]],
         [[12, 0], [12, 16]],
         [[10, 0], [10, 16]],
         [[8,0],[8,16]],
         [[6,0],[6,16]],
         [[4,0],[4,16]],
         [[2,0],[2,16]],
         ]
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

anchor = [[-1,-1],[20,20],]
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
    print("generate: path.png")


def draw_png_dot_graph(products,path):
    logger.info("drawing")
    plt.figure(figsize=(9, 9))
    G = nx.DiGraph()
    for p in anchor:
        G.add_node(-p[0]-p[1], label="", pos=(p[0], p[1]), col='white',size = 1)

    for p in products:
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]),col = 'grey',size = 100)

    for ind in range(len(shelf)):
        s = shelf[ind]
        id1 = str(s[0][0])
        id2 = - s[0][0]-1
        G.add_node(id1,label = "", pos=(s[0][0],s[0][1]),col = 'white',size = 1)
        G.add_node(id2,label = "", pos=(s[1][0],s[1][1]),col = 'white',size = 1)
        G.add_edge(id1,id2)
    pos = nx.get_node_attributes(G,'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    col =  nx.get_node_attributes(G, 'col').values()
    size = list(nx.get_node_attributes(G, 'size').values())
    nx.draw(G, pos=pos,   node_size = size,labels=node_labels,node_color = col,
            arrowstyle='-', arrows=True,
            arrowsize=30, edge_color='red',
            width=1
            )
    plt.savefig(path)
    logger.info("draw_png_graph generate: dot.png")

#
# p = [[1,8.2,10],[2,6.62,10],[4,16.4,12]]
# draw_png_dot_graph(p,"../data/path/dot.png")

def build_shelf():
   pass
