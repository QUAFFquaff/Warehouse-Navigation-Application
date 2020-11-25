
import networkx as nx
import matplotlib.pyplot as plt
import utils.LoggerFactory as LF

from pyecharts import options as opts
from pyecharts.charts import Graph

from objs.DataHandler import DataHandler
# shelf = [
#          [[20,0],[20,16]],
#
#          [[18, 0], [18, 16]],
#          [[16, 0], [16, 16]],
#          [[14, 0], [14, 16]],
#          [[12, 0], [12, 16]],
#          [[10, 0], [10, 16]],
#          [[8,0],[8,16]],
#          [[6,0],[6,16]],
#          [[4,0],[4,16]],
#          [[2,0],[2,16]],
#          ]
shelf = [[[0,0],[20,0]],
         [[0,2],[20,2]],
         [[0,4],[20,4]],
         [[0,6],[20,6]],
         [[0,8],[20,8]],
         [[0,10],[20,10]],
         [[0,12],[20,12]],
         [[0,14],[20,14]],
         [[0,16],[20,16]],
         [[0,18],[20,18]],
         [[0,20],[20,20]],
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
    # add anchor
    for p in anchor:
        G.add_node(-p[0]-p[1], label="", pos=(p[0], p[1]), col='white',size = 1)
    # add shelf
    for ind in range(len(shelf)):
        s = shelf[ind]
        id1 = str(s[0][0]) + str(s[0][1])
        id2 = str(s[1][0]) + str(s[1][1])
        G.add_node(id1, label="", pos=(s[0][0], s[0][1]), col='white', size=1)
        G.add_node(id2, label="", pos=(s[1][0], s[1][1]), col='white', size=1)
        G.add_edge(id1, id2, col='red')

    G.add_node(0,label = 'Smile!', pos=(0,0),col='grey',size = 100)
    for p in products:
        G.add_node(p[0],label = p[0], pos=(p[1],p[2]),col='grey',size = 100)

    G.add_edge(0, res[0],col = 'black',style = '->')
    G.add_edge(res[-1],0,col = 'black',style = '->')
    for i in range(1,len(res)):
        G.add_edge(res[i-1],res[i],col = "black",style = '->')
    pos = nx.get_node_attributes(G, 'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    col = nx.get_node_attributes(G, 'col').values()
    size = list(nx.get_node_attributes(G, 'size').values())
    edge_color = nx.get_edge_attributes(G, 'col').values()
    edge_style = nx.get_edge_attributes(G, 'style').values()
    nx.draw(G, pos=pos, node_size=size, labels=node_labels, node_color=col,
            arrowstyle='-', arrows=True,
            arrowsize=30, edge_color=edge_color,
            width=1
            )
    plt.savefig("data/path/path.png")
    logger.info("generate: path.png")


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
        id1 = str(s[0][0]) + str(s[0][1])
        id2 = str(s[1][0]) + str(s[1][1])
        G.add_node(id1, label="", pos=(s[0][0], s[0][1]), col='white', size=1)
        G.add_node(id2, label="", pos=(s[1][0], s[1][1]), col='white', size=1)
        G.add_edge(id1, id2, col='red')

    pos = nx.get_node_attributes(G,'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    col =  nx.get_node_attributes(G, 'col').values()
    size = list(nx.get_node_attributes(G, 'size').values())
    edge_color = nx.get_edge_attributes(G, 'col').values()
    nx.draw(G, pos=pos,   node_size = size,labels=node_labels,node_color = col,
            arrowstyle='-', arrows=True,
            arrowsize=30, edge_color=edge_color,
            width=1
            )
    plt.savefig(path)
    logger.info("draw_png_graph generate: dot.png")

#
# p = [[1,8.2,10],[2,6.62,10],[4,16.4,12]]
# draw_png_dot_graph(p,"../data/path/dot.png")

def draw_warehouse(products,path):
    logger.info("drawing")
    plt.figure(figsize=(9, 9))
    G = nx.Graph()
    for p in anchor:
        G.add_node(-p[0] - p[1], label="", pos=(p[0], p[1]), col='white', size=1)

    for p in products:
        G.add_node(p[0], label="", pos=(p[1], p[2]), col='grey', size=10)

    for ind in range(len(shelf)):
        s = shelf[ind]
        id1 = str(s[0][0])+str(s[0][1])
        id2 = str(s[1][0])+str(s[1][1])
        G.add_node(id1, label="", pos=(s[0][0], s[0][1]), col='white', size=1)
        G.add_node(id2, label="", pos=(s[1][0], s[1][1]), col='white', size=1)
        G.add_edge(id1, id2, col='red')

    pos = nx.get_node_attributes(G, 'pos')
    node_labels = nx.get_node_attributes(G, 'label')
    col = nx.get_node_attributes(G, 'col').values()
    size = list(nx.get_node_attributes(G, 'size').values())
    edge_color = nx.get_edge_attributes(G, 'col').values()
    nx.draw(G, pos=pos, node_size=size,  node_color=col,
            arrowstyle='-', arrows=True,
            arrowsize=30, edge_color=edge_color,
            width=1
            )
    plt.savefig(path)
    logger.info("draw_png_graph generate: warehouse.png")

def draw_warehouse_html(shelf_list, file_name):
    logger.info("start drawing warehouse html graph")
    nodes = []
    for ind,node in enumerate(shelf_list):
        nodes.append({
            "x": node[0],
            "y": node[1],
            "id": ind,
            'is_fixed': True,
            "name": "("+str(node[0])+','+str(node[1])+')',
            "symbolSize": 14,
            "itemStyle": {"normal": {"color": 'grey'}},
            "categories": 0,
            "symbol": "square"
        })

    edges = []
    (
        Graph(init_opts=opts.InitOpts(width="641px", height="441px"))
            .add(
            series_name="",
            nodes=nodes,
            links=edges,
            layout="none",
            #         is_roam=True,
            is_focusnode=True,
            categories=[{"name":'shelf'}],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.9, opacity=0.9, color="source"),
            #             linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
            title_opts=opts.TitleOpts(title="Warehouse products distribution"),
        )
            .render(file_name)
    )
    print("done")

def draw_dots_html(shelf_list,p_nodes, file_name):
    logger.info("start drawing products html graph")
    nodes = []
    for ind,node in enumerate(shelf_list):
        nodes.append({
            "x": node[0],
            "y": node[1],
            "id": -ind,
            'is_fixed': True,
            "name": "("+str(node[0])+','+str(node[1])+')',
            "symbolSize": 14,
            "itemStyle": {"normal": {"color": 'grey'}},
            "categories": 0,
            "symbol": "square"
        })
    logger.info("finish shelf")
    logger.info(p_nodes)
    for node in p_nodes:
        nodes.append({
            "x": node[1],
            "y": node[2],
            "id": node[0],
            'is_fixed': True,
            "name": str(node[0]),
            "symbolSize": 14,
            "itemStyle": {"normal": {"color": 'blue'}},
            "categories": 1,
            "symbol": "square"
        })
    logger.info("finish products")
    edges = []
    (
        Graph(init_opts=opts.InitOpts(width="641px", height="441px"))
            .add(
            series_name="",
            nodes=nodes,
            links=edges,
            layout="none",
            #         is_roam=True,
            is_focusnode=True,
            categories=[{"name":'shelf'},{"name":'products'}],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.9, opacity=0.9, color="source"),
            #             linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
            title_opts=opts.TitleOpts(title="Warehouse products distribution"),
        )
            .render(file_name)
    )
    print("done")


def draw_path_html(shelf_list,p_nodes,path, file_name):
    logger.info("start drawing products html graph")
    nodes = []
    for ind, node in enumerate(shelf_list):
        nodes.append({
            "x": node[0],
            "y": node[1],
            "id": -ind,
            'is_fixed': True,
            "name": "(" + str(node[0]) + ',' + str(node[1]) + ')',
            "symbolSize": 14,
            "itemStyle": {"normal": {"color": 'grey'}},
            "categories": 0,
            "symbol": "square"
        })
    logger.info("finish shelf")
    logger.info(p_nodes)
    for node in p_nodes:
        nodes.append({
            "x": node[1],
            "y": node[2],
            "id": node[0],
            'is_fixed': True,
            "name": str(node[0]),
            "symbolSize": 14,
            "itemStyle": {"normal": {"color": 'blue'}},
            "categories": 1,
            "symbol": "square"
        })
    logger.info("finish products")

    edges = []
    # for node in path:
    #     nodes.append({
    #         "x": pos[node][0],
    #         "y": pos[node][1],
    #         "id": node,
    #         "name": name[node] + name_to_cn.get(name[node], ""),
    #         "symbolSize": size[node],
    #         "itemStyle": {"normal": {"color": colors[node]}},
    #         "categories": "a"
    #     })
    #     nodes_id.append(node)
    #
    # for edge in G.edges():
    #     if colors[edge[0]] in ['orange', 'blue']:
    #         edges.append({"source": nodes_id.index(edge[0]),
    #                       "target": nodes_id.index(edge[1])
    #                       })
    #     else:
    #         edges.append({"source": nodes_id.index(edge[1]),
    #                       "target": nodes_id.index(edge[0])
    #                       })
    #
    # links = [opts.GraphLink(source=nodes_id.index(e[0]), target=nodes_id.index(e[1])) for e in G.edges()]
    (
        Graph(init_opts=opts.InitOpts(width="641px", height="441px"))
            .add(
            series_name="",
            nodes=nodes,
            links=edges,
            layout="none",
            #         is_roam=True,
            is_focusnode=True,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.9, opacity=0.9, color="source"),
            #             linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
            title_opts=opts.TitleOpts(title="path"),
        )
            .render(file_name)
    )
    print("done")

# def draw_html(G, file_name):
#     pos = nx.get_node_attributes(G, 'pos')
#     colors = nx.get_node_attributes(G, 'color')
#     size = nx.get_node_attributes(G, 'size')
#     name = nx.get_node_attributes(G, 'desc')
#     nodes = []
#     nodes_id = []
#     for node in G.nodes():
#         nodes.append({
#             "x": pos[node][0],
#             "y": pos[node][1],
#             "id": node,
#             "name": name[node] + name_to_cn.get(name[node], ""),
#             "symbolSize": size[node],
#             "itemStyle": {"normal": {"color": colors[node]}},
#             "categories": "a"
#         })
#         nodes_id.append(node)
#
#     edges = []
#     for edge in G.edges():
#         if colors[edge[0]] in ['orange', 'blue']:
#             edges.append({"source": nodes_id.index(edge[0]),
#                           "target": nodes_id.index(edge[1])
#                           })
#         else:
#             edges.append({"source": nodes_id.index(edge[1]),
#                           "target": nodes_id.index(edge[0])
#                           })
#
#     links = [opts.GraphLink(source=nodes_id.index(e[0]), target=nodes_id.index(e[1])) for e in G.edges()]
#     (
#         Graph(init_opts=opts.InitOpts(width="1600px", height="800px"))
#             .add(
#             series_name="",
#             nodes=nodes,
#             links=edges,
#             layout="none",
#             #         is_roam=True,
#             is_focusnode=True,
#             label_opts=opts.LabelOpts(is_show=False),
#             linestyle_opts=opts.LineStyleOpts(width=0.9, opacity=0.9, color="source"),
#             #             linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
#         )
#             .set_global_opts(
#             legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
#             title_opts=opts.TitleOpts(title="数据提取关系图"),
#         )
#             .render(file_name)
#     )
#     print("done")
# nodes = [[1,2,3],[2,12,23],[4,42,24]]
# draw_warehouse_html(nodes,'test.html')