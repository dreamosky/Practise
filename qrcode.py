import qrcode

img = qrcode.make('I love you')
# img <qrcode.image.pil.PilImage object at 0x1044ed9d0>

with open('test.png', 'wb') as f:
    img.save(f)
