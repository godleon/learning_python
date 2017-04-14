from collections import defaultdict

x = defaultdict(list)
x['a'].append(1)
x['a'].append(2)
x['b'].append(4)

print(x)