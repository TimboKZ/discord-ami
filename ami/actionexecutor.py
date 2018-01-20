from ami.actions.weightedrelationships import WeightedRelationshipsAction


class ActionExecutor:
    def __init__(self, config):
        self.config = config
        self.action = None
        self.action_name = self.config.get('action')

        if self.action_name == 'weighted-relationships':
            self.action = WeightedRelationshipsAction(config)
        else:
            raise NotImplementedError('Action {0} is not supported!'.format(self.action_name))

    def execute_action(self, channels_with_messages):
        print('Executing action `{0}`...'.format(self.action_name))
        self.action.execute(channels_with_messages)
        self.action.save_figure()
        self.action.save_graph()
        print('Finished executing action!')
