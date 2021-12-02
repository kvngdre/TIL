"""Today I'm learning about the strftime method of the time module"""

from time import strftime, gmtime, localtime

a = strftime("%H:%M:%S", localtime())  # Prints the 24 hour time format, remember all uppercase for 24 time format.
print(a)

s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
print("Example 1:", s)

s1 = strftime("%A, %D %B %Y %H:%M:%S + 0000", gmtime())
print("Example 2: ", s1)

s2 = strftime("%c")
print("Example 3: ", s2)

s3 = strftime("%C")
print("Example 3: ", s3)
