"""Today I'm learning about the strftime method of the time module"""

from time import strftime, gmtime, localtime


a = strftime("%H:%M:%S", localtime())
# So to remember this I try to memorize that time in 24h format = ALL UPPERCASE.
print(a)

s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
# I had to make an association in my head that "a-d-d" spelt with last letter back is:
# %a=day of the week[Thurs].....(letter)
# %d=the number day of the week.(Number)
# %b=Short name of the month....(letter)
# and %Y=full numeric year......(Number) -> {1010},
# You gerrit? if you don't gerrit forget about it. 😁
# it works the same for localtime() function
print("Example 1:", s)

"""Full Day Name_ seems to print a short date with all numbers m/d/y full month name year per usual."""
s1 = strftime("%A, %D %B %Y %H:%M:%S + 0101", localtime())
# For this I tried to relate it to the previous 1010 so,
# %A=full name of day of the week[THURSDAY].......(Uletter) 0
# %D=month starts full short / date all numbers....(Number) 1
# %B=full name of month in words..................(Uletter) 0
# %Y=full numeric year.............................(Number) 1  -> {0101}
print("Example 2:", s1)

s2 = strftime("%c")
# I used the %D short / date as my reference and dumped the HMS time in between day and year
print("Example 3:", s2)

s3 = strftime("%R")
# prints the 24h time format no seconds
print("Example 4:", s3)

s4 = strftime("%r")
# prints the 12h time format
print("Example 4:", s4)

s5 = strftime("%a, %d %b %Y %I:%M:%S + 0000", gmtime())
# %I=changes the time format to 12h.
print("Example 5:", s5)


s6 = strftime("%r, %T ", gmtime())
# %T=current time == %H:%M:%S
print("Example 6:", s6)

s7 = strftime("%x, %X, %y, %Y")
# %x=day starts short / date all numbers
# %X=24h time with seconds included
# %y=the year youngin'
# %Y=full yer
print("Example 7:", s7)

s8 = strftime("%r, %z, %Z")
# %r=12 h format with seconds
# %z=time zone in GMT
# %Z=time zone in West African...
print("Example 8:", s8)
