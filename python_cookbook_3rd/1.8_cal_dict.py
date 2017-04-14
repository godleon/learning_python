
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(prices.values())
print(prices.keys())
zipped = zip(prices.values(), prices.keys())
print(zipped)
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))