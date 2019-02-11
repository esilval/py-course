# List

# Basic example
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# Another example build a list of unicode codepoints from a string
codes = [ord(symbol) for symbol in symbols]
print(codes)

# create a list with listcomp
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# map/filter composition
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)