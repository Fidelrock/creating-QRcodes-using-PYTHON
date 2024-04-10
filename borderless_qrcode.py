# Adding border to the qrcode

import segno

qrcode = segno.make_qr("Allan likes Joking")
qrcode.save("borderless_qrcode.png",
scale=5,
border = 10
)