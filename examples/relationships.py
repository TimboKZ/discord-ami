from ami.core import Ami
import json

botConfig = json.load(open('bot-config.json'))

config = {
    'token': botConfig.get('token'),
    'email': botConfig.get('email'),
    'password': botConfig.get('password'),
    'action': 'weighted-relationships',
    'serverId': '317924870950223872',
    'channels': [
        {
            'id': '317924870950223872',
            'messageLimit': 10000,
        },
        {
            'id': '317933848203755521',
            'messageLimit': 10000,
        },
        {
            'id': '320219158593667072',
            'messageLimit': 10000,
        },
        {
            'id': '342393014985031681',
            'messageLimit': 10000,
        },
    ],
    'graphOutput': 'weighted-relationships.gexf',
    'figureOutput': 'weighted-relationships.png',
}

ami = Ami(config)
ami.run()
