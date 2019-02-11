# Generator expressions

# Initializing a tuple and an array from a genexp
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

import array
array.array('I', (ord(symbol) for symbol in symbols))

# Cartesian product with genexp
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)