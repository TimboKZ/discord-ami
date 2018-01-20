from ami.actions.action import Action
import networkx as nx


class WeightedRelationshipsAction(Action):
    def __init__(self, config):
        super().__init__(config)

        self.graph = nx.DiGraph()

    def execute(self, channels_with_messages):

        for channel_data in channels_with_messages:
            print('Processing channel `{0}`...'.format(channel_data.get('channel').name))
            message_queue = channel_data.get('messageQueue')
            previous_author = None
            while message_queue:
                message = message_queue.pop()
                author = message.get('author')
                self.graph.add_node(author)
                # TODO: Analyse content of messages for mentions
                if previous_author is not None and author is not previous_author:
                    if self.graph.has_edge(author, previous_author):
                        self.graph[author][previous_author]['weight'] += 1
                    else:
                        self.graph.add_edge(author, previous_author, weight=1)
                previous_author = author
