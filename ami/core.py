from ami.discordscanner import DiscordScanner
from ami.actionexecutor import ActionExecutor
import asyncio


class Ami:
    def __init__(self, config):
        self.config = config
        self.executor = ActionExecutor(self.config)
        self.scanner = DiscordScanner(config)

    def run(self):
        print('Starting Ami...')
        print('-----')
        self.scanner.run(self.process_channels_with_messages)

    def process_channels_with_messages(self, channels_with_messages):
        print('-----')
        self.executor.execute_action(channels_with_messages)
