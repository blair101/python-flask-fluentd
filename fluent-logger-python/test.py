
from fluent import sender
from fluent import event


sender.setup('fluentd.test', host='localhost', port=24224)

event.Event('follow', { # send event to fluentd, with 'app.follow' tagevent.Event('follow', {
  'from': 'userA',
  'to':   'userB'
})


