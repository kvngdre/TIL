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
qr = qrcode.QRCode(
    version=22,  # QR Codes have 40 different versions
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Up to 7% error correction
    box_size=10,  # The size of the image
    border=5,  # size of the borer measured in pixels.
)
qr.add_data(link)
qr.make(fit=True)

qr_image = qr.make_image(fill_color='black', back_color='red')
qr_image.save('image2.png')