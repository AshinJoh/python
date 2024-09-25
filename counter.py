from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)

print(counter)
print(counter['banana'])