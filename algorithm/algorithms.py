



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
    print('in')
    res = [products[i-1][0] for i in range(1,len(res_ind)-1)]
    print('res: ',res)
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
    # nx.draw(G, pos=pos,  node_size=500, labels=node_labels,
    #         arrowstyle='->', arrows=True,
    #         arrowsize=30, edge_color='red',
    #         width=1
    #         )
    print("大傻逼")
    nx.draw(G, pos=pos,  node_size=500, labels=node_labels, font='bond',
            arrowstyle='->', arrows=True,
            arrowsize=30, edge_color='red',
            width=1, directed=True
            )
    plt.savefig("data/path/path.png")
    print("generate: path.png")
    pass

def draw_png_dot_graph(products):
    #import pdb
    #pdb.set_trace()
    plt.figure(figsize=(9, 9))
    #pdb.set_trace()
    G = nx.DiGraph()
   # pdb.set_trace()
    for p in products:
      #  pdb.set_trace()
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]))
    pos = nx.get_node_attributes(G,'pos')
    #pdb.set_trace()
    node_labels = nx.get_node_attributes(G, 'label')
    #pdb.set_trace()
    print("123")
    # nx.draw(G, pos=pos,  node_size=500, labels=node_labels,
    #         arrowstyle='->', arrows=True,
    #         arrowsize=30, edge_color='red',
    #         width=1
    #         )
    nx.draw(G, pos=pos,  node_size=500, labels=node_labels, font='bond',
            arrowstyle='->', arrows=True,
            arrowsize=30, edge_color='red',
            width=1, directed=True
            )

    # plt.show()
    # G = nx.house_graph()
    # pos = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1), 4: (0.5, 2.0)}
    #
    # nx.draw_networkx_nodes(G, pos, node_size=2000, nodelist=[4])
    # nx.draw_networkx_nodes(G, pos, node_size=3000, nodelist=[0, 1, 2, 3], node_color="b")
    # nx.draw_networkx_edges(G, pos, alpha=0.5, width=6)
    #pdb.set_trace()
    plt.savefig("data/path/dot.png")
    print("generate: dot.png")
    pass
