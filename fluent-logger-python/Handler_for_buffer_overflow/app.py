'''
  Handler for buffer overflow

    You can inject your own custom proc to handle buffer overflow in the event of connection failure. This will mitigate the loss of data instead of simply throwing data away.
'''

from fluent import sender
from fluent import event

import time

import msgpack
from io import BytesIO

def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)

# for local fluent
logger = sender.FluentSender('app')

# for remote fluent
logger = sender.FluentSender('app', host='localhost', port=24224)

# Specify optional time
cur_time = int(time.time())

# logger.emit_with_time('follow', cur_time, {'from': 'userA', 'to':'userB'})

# Use nanosecond
logger = sender.FluentSender('app', nanosecond_precision=True)

logger = sender.FluentSender('app', host='localhost', port=24224, buffer_overflow_handler=overflow_handler)

logger.emit('follow', {'from': 'userA', 'to': 'userB'})

logger.emit_with_time('follow', time.time(), {'from': 'userA', 'to': 'userB'})

logger.close()