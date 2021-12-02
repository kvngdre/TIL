"""Today I'm learning about the strftime method of the time module"""

from time import strftime, gmtime, localtime

created = "Created Thurs 02 Dec 2021 22:43"
track = "Amaarae - 3AM"

a = strftime("%H:%M:%S", localtime())  # So to remember this I try to memorize that time in 24h format = ALL UPPERCASE.
print(a)

s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
# I had to make an association in my head that "a-d-d" spelt with last letter back is:
# %a=day of the week[Thurs].....(letter)
# %d=the number day of the week.(Number)
# %b=Short name of the month....(letter)
# and %Y=full numeric year......(Number) -> {1010},
# You gerrit? if you don't gerrit forget about it. 😁
# it works the same for localtime() function
# print(strftime("%a, %d %b %Y %H:%M:%S + 1010", localtime()))
print("Example 1:", s)

"""Full Day Name_ seems to print a short date with all numbers m/d/y full month name year per usual."""
s1 = strftime("%A, %D %B %Y %H:%M:%S + 0000", gmtime())
print("Example 2: ", s1)

s2 = strftime("%c")
print("Example 3: ", s2)

# Please note MOTY: month of the year
# please note DOTY: Day of the year
# Simple representation
s3 = strftime(" %R ")
print("Example 3: ", s3)
