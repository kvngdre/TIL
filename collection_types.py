"""Learning about how to count for different collection types"""

o = ['pink', 'pink', 2, 3, 3, 'Red']

print(o.count('pink'))  # for lists only.

o = tuple(o)

print(sum(i == 'pink' for i in o))  # Because bools are ints TRUE: 1

from operator import countOf

print(countOf(o, 'pink'))

from collections import Counter

print(Counter(o)['pink'])

import calendar
s = calendar.TextCalendar(calendar.SUNDAY)
s.prmonth(2021, 12)

# TO output the calender as HTML
from IPython.display import HTML
HTML(s.formatmonth(2021, 12))
