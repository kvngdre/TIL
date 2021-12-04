"""Today I learnt about how to count elements and their occurrences for different collection types"""

o = ['pink', 'pink', 2, 3, 3, 'Red']
print(o.count('pink'))  # for lists only.

o = tuple(o)
print(sum(i == 'pink' for i in o))  # Because booleans are integers TRUE = 1

from operator import countOf
print(countOf(o, 'pink'))

from collections import Counter
print(Counter(o))  # Returns a dict-like of the value: count as the key-value pair.
print(Counter(o)['pink'])


