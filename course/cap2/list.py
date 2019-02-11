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

