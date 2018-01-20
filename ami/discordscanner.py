from collections import deque
import discord
import numpy


class DiscordScanner(object):
    def __init__(self, config):
        self.config = config
        self.client = discord.Client()

    def run(self, callback):
        print('Connecting to Discord...')

        @self.client.event
        async def on_ready():
            print('Logged in as: {0}'.format(self.client.user.name))
            callback(await self.scan_messages())
            await self.client.close()

        if self.config.get('token') is not None:
            self.client.run(self.config.get('token'))
        else:
            self.client.run(self.config.get('email'), self.config.get('password'))

    async def scan_messages(self):
        print('Scanning messages...')
        server = self.client.get_server(self.config.get('serverId'))
        print('Server: {0}'.format(server.name))

        channels_with_messages = numpy.empty(len(self.config.get('channels')), dtype=object)

        index = 0
        for scanChannel in self.config.get('channels'):
            channel = self.client.get_channel(scanChannel.get('id'))
            message_queue = await self.fetch_messages(channel, scanChannel.get('messageLimit'))
            channels_with_messages[index] = {
                'channel': channel,
                'messageQueue': message_queue,
            }
            index += 1

        print('Finished scanning!')

        return channels_with_messages

    async def fetch_messages(self, channel, count):
        message_queue = deque()
        print('Fetching {0} message(s) from channel `{1}`...'.format(count, channel.name), flush=True)
        message_count = 0
        async for message in self.client.logs_from(channel, limit=count):
            message_queue.append({
                'author': message.author.display_name,
                'content': message.content,
            })
            message_count += 1
        print('Fetched {0} message(s).'.format(message_count))
        return message_queue
