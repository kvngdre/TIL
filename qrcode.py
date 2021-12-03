"""
Today I learnt about making QR codes with Python.
"""

import qrcode

# We can take the easy route and just 'make' and 'save' the QR code image file.
link = 'https://www.google.com'
word = 'Hello World!'
qrcode.make(link)  # Can be a link
qrcode.make(word)  # Could be a word or phase or sentence too.

# Say we wanted to customize our QR Code image, like the size and color.

