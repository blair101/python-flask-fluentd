import logging

import msgpack
from io import BytesIO

'''load logging config'''
import logging.config
import yaml


def load():

    with open('logging.yaml') as fd:
        print(fd)
        conf = yaml.load(fd)
        print(conf)
        print(conf['logging'])

    logging.config.dictConfig(conf['logging'])

def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)

def main():

    l = logging.getLogger('fluent.test')

    l.info({
        'from': 'userA-3',
        'to': 'userB-4'
    })
    l.info('{"from": "userC", "to": "userD"}')
    l.info("This log entry will be logged with the additional key: 'message'.")

if __name__ == '__main__':

    load()
    main()