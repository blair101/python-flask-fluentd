import logging
import yaml

with open('logging.yaml') as fd:
    print(fd)
    conf = yaml.load(fd)
    print(conf)
    print(conf['logging'])

logging.config.dictConfig(conf['logging'])