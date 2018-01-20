import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx


class Action:
    def __init__(self, config):
        self.config = config
        self.graph = None

    def execute(self, channels_with_messages):
        raise NotImplemented

    def save_graph(self):
        nx.write_gexf(self.graph, self.config.get('graphOutput'))

    def save_figure(self):
        font_files = font_manager.findSystemFonts()
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        mpl.rcParams['font.family'] = 'Arial'
        plt.figure(figsize=(7, 7))
        plt.axis('off')
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos, cmap=plt.get_cmap('jet'), node_color='0.65',
                               node_size=500, node_shape='o')
        nx.draw_networkx_labels(self.graph, pos, font_size=4, font_family='Arial')
        nx.draw_networkx_edges(self.graph, pos, arrows=False, cmap=plt.get_cmap('jet'), edge_color='0.80')
        plt.savefig(self.config.get('figureOutput'), dpi=600)
