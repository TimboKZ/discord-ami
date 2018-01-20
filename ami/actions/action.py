import matplotlib.pyplot as plt
import networkx as nx
import math


class Action:
    def __init__(self, config):
        self.config = config
        self.graph = None

    def execute(self, channels_with_messages):
        raise NotImplemented

    def load_graph(self):
        self.graph = nx.read_gexf(self.config.get('graphInput'))

    def save_graph(self):
        nx.write_gexf(self.graph, self.config.get('graphOutput'))

    def save_figure(self):
        G = self.graph.to_undirected()

        plt.figure(figsize=(7, 7))
        plt.axis('off')
        pos = nx.spring_layout(G, k=6, iterations=20)
        nx.draw_networkx_nodes(G, pos, node_color='0.65', node_size=200, node_shape='o')
        nx.draw_networkx_labels(G, pos, font_size=4, font_family='Arial')

        def normalize(x):
            return min([math.log(float(x)) / 6, 1])

        edge_labels = [normalize(d['weight']) for u, v, d in G.edges(data=True)]
        print(edge_labels)

        nx.draw_networkx_edges(G, pos, arrows=False, edge_cmap=plt.get_cmap('Greys'),
                               edge_color=edge_labels, width=edge_labels, alpha=0.9)
        plt.savefig(self.config.get('figureOutput'), dpi=600, bbox_inches='tight')
