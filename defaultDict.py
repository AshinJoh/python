from collections import defaultdict

dd = defaultdict(list)

dd["fruits"].append('apple')
dd["fruits"].append('orange')

print(dd['fruits'])
print(dd['vegetables'])
