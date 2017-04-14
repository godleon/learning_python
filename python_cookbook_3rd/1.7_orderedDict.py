from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print(d)
print(json.dumps(d))


e = {}
e['foo'] = 1
e['bar'] = 2
e['spam'] = 3
e['grok'] = 4
print(e)
print(json.dumps(e))