from ami.discordscanner import DiscordScanner
from ami.actionexecutor import ActionExecutor
import asyncio


class Ami:
    def __init__(self, config):
        self.config = config
        self.executor = ActionExecutor(self.config)

    def run(self):
        print('Starting Ami...')
        if self.executor.need_to_fetch_messages():
            print('-----')
            scanner = DiscordScanner(self.config)
            scanner.run(self.process_channels_with_messages)
        else:
            self.executor.execute_action_standalone()

    def process_channels_with_messages(self, channels_with_messages):
        print('-----')
        self.executor.execute_action_with_messages(channels_with_messages)
