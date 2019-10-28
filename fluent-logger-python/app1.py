
from fluent import sender
from fluent import event

import time

'''
   FluentSender Interface
   
     sender.FluentSender is a structured event logger for Fluentd.

     By default, the logger assumes fluentd daemon is launched locally. You can also specify remote logger by passing the options.
'''

# for local fluent
logger = sender.FluentSender('app')

# for remote fluent
logger = sender.FluentSender('app', host='localhost', port=24224)

# Specify optional time
cur_time = int(time.time())

# logger.emit_with_time('follow', cur_time, {'from': 'userA', 'to':'userB'})

# Use nanosecond
logger = sender.FluentSender('app', nanosecond_precision=True)

logger.emit('follow', {'from': 'userA', 'to': 'userB'})

logger.emit_with_time('follow', time.time(), {'from': 'userA', 'to': 'userB'})

logger.close()